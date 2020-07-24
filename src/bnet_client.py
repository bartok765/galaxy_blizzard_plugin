import asyncio
import functools
import logging
import struct
from typing import List

from fnvhash import fnv1a_32
from galaxy.api.errors import BackendError
from google.protobuf.message import Message
from google.protobuf.text_format import MessageToString
from requests import utils

from bnet import (
    authentication_service_pb2,
    connection_service_pb2,
    friends_service_pb2, friends_types_pb2,
    presence_service_pb2, presence_types_pb2,
    rpc_pb2,
)

log = logging.getLogger(__name__)
log.setLevel = logging.INFO


class BNetClient:
    def __init__(self, authentication_client):
        self._authentication_client = authentication_client
        self._BACKEND_SERVER_HOST = None
        self._BACKEND_SERVER_PORT = 1119

        self._AUTHENTICATION_SERVER_SERVICE = "bnet.protocol.authentication.AuthenticationServer"
        self._AUTHENTICATION_CLIENT_SERVICE = "bnet.protocol.authentication.AuthenticationClient"
        self._CHALLENGE_SERVICE = "bnet.protocol.challenge.ChallengeService"
        self._PRESENCE_SERVICE = "bnet.protocol.presence.PresenceService"
        self._FRIENDS_SERVICE = "bnet.protocol.friends.FriendsService"
        self._NOTIFICATION_SERVICE = "bnet.protocol.notification.NotificationService"
        self._RESOURCES_SERVICE = "bnet.protocol.resources.Resources"
        self._CHANNEL_INVITATION_SERVICE = "bnet.protocol.channel_invitation.ChannelInvitationService"

        self._RESPONSE_SERVICE = "response"
        self._RESPONSE_SERVICE_ID = 254
        self._CONNECTION_SERVICE = "bnet.protocol.connection.ConnectionService"
        self._CONNECTION_SERVICE_ID = 0

        self._imported_services = (
            self._AUTHENTICATION_SERVER_SERVICE,
            self._PRESENCE_SERVICE,
            self._FRIENDS_SERVICE,
            self._NOTIFICATION_SERVICE,
            self._RESOURCES_SERVICE,
        )

        self._imported_services_map = {
            self._RESPONSE_SERVICE: self._RESPONSE_SERVICE_ID,
            self._CONNECTION_SERVICE: self._CONNECTION_SERVICE_ID
        }
        self._exported_services = (
            self.ExportedService(1, "bnet.protocol.authentication.AuthenticationClient"),
            self.ExportedService(2, "bnet.protocol.challenge.ChallengeNotify"),
            self.ExportedService(3, "bnet.protocol.account.AccountNotify"),
            self.ExportedService(4, "bnet.protocol.account.PresenceNotify"),
            self.ExportedService(5, "bnet.protocol.friends.FriendsNotify"),
            self.ExportedService(6, "bnet.protocol.channel.ChannelSubscriber"),
            self.ExportedService(7, "bnet.protocol.channel_invitation.ChannelInvitationNotify"),
            self.ExportedService(8, "bnet.protocol.connection.ConnectionService"),
            self.ExportedService(9, "bnet.protocol.notification.NotificationListener"),
        )

        self._exported_services_map = {
            # service_id: { method_id: callback }
            1: {5: self._on_authentication__logon},
            # 2: {3: self._on_challenge__challenge_external_request},
            # 5: {1: self._on_friends__friend_notification, 3: self._on_friends__invitation_notification},
            # 6: {1: self._on_channel__add_notification, 6: self._on_channel__update_channel_state_notification},
            8: {3: self._on_connection__echo_request, 4: self._on_connection__disconnect_notification},
            # 9: {1: self._on_notification__notification},
        }

        self._object = 1
        self._token = 0
        self._token_callbacks = {}
        self._account_id = None
        self._game_account_id = None
        self.reader = None
        self.writer = None
        self.authenticated = False

    class BNetService:
        def __init__(self, service_name):
            self.name = service_name
            self.methods = {}

    class ExportedService:
        def __init__(self, id, name):
            self.id = id
            self.name = name
            self.hash = fnv1a_32(bytes(name, "UTF-8"))
            self.methods = {}

    class ServiceWrapper:
        def __init__(self, callback):
            self.callback = callback

    class AccountInfo:
        def __init__(self, fields: List[presence_types_pb2.Field]):
            self.battle_tag = None
            self.full_name = None
            self.game_account_ids = []

            for f in fields:
                if f.key.group != 1:
                    continue

                # LIST OF POSSIBLE KEYS / VALUES:
                # key.field = 1 (full_name: value.string_value) only works for RealId friends, others will FAIL WITH ERROR, return e.g. "Firstname Lastname"
                # key.field = 2 (???: value.string_value) only returns for some friends, returns ""
                # key.field = 3 (game_account_id: value.entityid_value) only returns for online friends, returns e.g. high: 144115197778542960 low: 116591225
                # > can be returned multiple times for different apps/games, where user is logged in (e.g. PC, Mobile etc.)
                # key.field = 4 (battle_tag: value.string_value) returns e.g. "Username#1234"
                # key.field = 5 (???: value.int_value) only returns for some friends, returns e.g. 1591116989396775 (microseconds timestamp)
                # key.field = 6 (???: value.int_value) returns e.g. 1592215097253865 (microseconds timestamp)
                # key.field = 7 (???: value.bool_value) returns false
                # key.field = 8 (???: value.int_value) return e.g. 1583607638026991 (microseconds timestamp)
                # key.field = 9 FAILS WITH ERROR
                # key.field = 10 FAILS WITH ERROR
                # key.field = 11 (???: value.bool_value) returns false

                if f.key.field == 1:
                    self.full_name = f.value.string_value.encode('utf-8')  # e.g. "Firstname Lastname"
                if f.key.field == 3:
                    self.game_account_ids.append(f.value.entityid_value)  # e.g. high: 144115197778542960 low: 131237370
                if f.key.field == 4:
                    self.battle_tag = f.value.string_value  # e.g. "Username#1234"

    class GameAccountInfo:
        def __init__(self, fields: List[presence_types_pb2.Field]):
            self.program = None
            self.rich_presence = None
            self.is_away = None

            for f in fields:
                if f.key.group != 2:
                    continue

                # LIST OF POSSIBLE KEYS / VALUES:
                # key.field = 1 (is online: value.bool_value) returns true
                # key.field = 2 (???: value.int_value) only returns for certain games (S2, ...), returns e.g. 0
                # key.field = 3 (program: value.fourcc_value) returns e.g. "BSAp", "Pro" (for Overwatch)
                # key.field = 4 (???: value.int_value) returns e.g. 1584194739362351 (microseconds timestamp)
                # key.field = 5 (battle_tag: value.string_value) returns e.g. "Username#1234"
                # key.field = 6 FAILS WITH ERROR
                # key.field = 7 (account_id: value.entityid_value) returns e.g. high: 72057594037927936 low: 101974425
                # key.field = 8 (rich_presence: value.message_value) only returns when user is in-game, returns e.g. "\rorP\000\025aorp\030\025" or ""\r2S\000\000\025SRPR\030\000""
                # key.field = 9 (???: value.int_value) returns e.g. 1584228809551117 (microseconds timestamp)
                # key.field = 10 (is_away: value.bool_value) returns true/false
                # key.field = 11 (???: value.int_value) returns e.g. 1595601904845128 (microseconds timestamp)

                if f.key.field == 3:
                    self.program = f.value.fourcc_value  # e.g. "App", "BSAp" or "Pro" (for Overwatch)
                if f.key.field == 8:
                    self.rich_presence = presence_types_pb2.RichPresence().ParseFromString(f.value.message_value)  # e.g. "\rorP\000\025aorp\030\025"
                if f.key.field == 10:
                    self.is_away = f.value.bool_value

    def _next_object(self):
        self._object += 1
        return self._object

    def _next_token(self):
        self._token += 1
        self._token = self._token % 512
        return self._token

    def _set_backend_server_host(self, region):
        self._BACKEND_SERVER_HOST = "{}.actual.battle.net".format(region)

    def _log_received_message(self, name, header, message: Message):
        log.debug(f"fetched {name} token: {header.token} body: {MessageToString(message, as_one_line=True)}")

    async def _send_message(self, service_name, method_id, body, callback=None):
        if self.writer is None:
            raise BackendError("connection to battle.net is closed")

        header = rpc_pb2.Header()
        header.service_id = self._imported_services_map[service_name]

        if header.service_id != self._RESPONSE_SERVICE_ID:
            header.method_id = method_id
            header.token = self._next_token()
        else:
            header.method_id = 0
            header.token = method_id

        header.size = body.ByteSize()

        if callback:
            self._token_callbacks[header.token] = callback

        log.debug(f"protobuf sending data: service {header.service_id} ({service_name}) method {header.method_id} token {header.token}")

        self.writer.write(struct.pack("!H", header.ByteSize()))
        self.writer.write(header.SerializeToString())
        self.writer.write(body.SerializeToString())
        await self.writer.drain()

    async def _on_presence__query_game_account(self, future: 'asyncio.Future[GameAccountInfo]', header, body):
        if not body:
            log.warning("failed presence:query_response")
            future.set_result(self.GameAccountInfo([]))
            return

        response = presence_service_pb2.QueryResponse()
        response.ParseFromString(body)

        self._log_received_message("presence:query_response", header, response)

        future.set_result(self.GameAccountInfo(response.field))

    async def _on_presence__query_account(self, future: 'asyncio.Future[AccountInfo]', header, body):
        if not body:
            log.error("failed presence:query_response")
            future.set_result(self.AccountInfo([]))
            return

        response = presence_service_pb2.QueryResponse()
        response.ParseFromString(body)

        self._log_received_message("presence:query_response", header, response)

        future.set_result(self.AccountInfo(response.field))

    async def _on_friends__subscribe_to_friends(self, future: 'asyncio.Future[List[friends_types_pb2.Friend]]', header, body):
        if not body:
            log.error("failed friends:subscribe_to_friends_response")
            future.set_result([])
            return

        response = friends_service_pb2.SubscribeToFriendsResponse()
        response.ParseFromString(body)

        self._log_received_message("friends:subscribe_to_friends_response", header, response)

        future.set_result(response.friends)

    async def _on_authentication__select_game_account(self, header, body):
        log.info("successfully authenticated with battle.net")
        self.authenticated = True

    async def _on_authentication__logon(self, header, body):
        if header.status != 0:
            raise BackendError("failed to authenticate with battle.net")

        response = authentication_service_pb2.LogonResult()
        response.ParseFromString(body)

        self._log_received_message("authentication:logon_result", header, response)

        self._account_id = response.account
        self._game_account_id = response.game_account[0]

        await self._send_message(self._AUTHENTICATION_SERVER_SERVICE, 4, self._game_account_id, self._on_authentication__select_game_account)

    async def _on_connection__echo_request(self, header, body):
        request = connection_service_pb2.EchoRequest()
        request.ParseFromString(body)

        self._log_received_message("connection:echo_request", header, request)

        response = connection_service_pb2.EchoResponse()
        response.time = request.time
        response.payload = request.payload

        await self._send_message(self._RESPONSE_SERVICE, header.token, response)

    async def _on_connection__disconnect_notification(self, header, body):
        response = connection_service_pb2.DisconnectNotification()
        response.ParseFromString(body)

        self._log_received_message("connection:disconnect_notification", header, response)

        # error_code: 3014

        await self.disconnect()

    async def _on_connection__connect_response(self, header, body):
        response = connection_service_pb2.ConnectResponse()
        response.ParseFromString(body)

        self._log_received_message("connection:connect_response", header, response)

        self._imported_services_map.update(zip(self._imported_services, response.bind_response.imported_service_id))

        await self.logon()

    async def _watch_receive_message(self):
        while True:
            await self._receive_message()

    async def _receive_message(self):
        if self.reader is None:
            raise BackendError("connection to battle.net is closed")

        header_len_buf = await self.reader.read(2)
        if not header_len_buf:
            return
        if len(header_len_buf) < 2:
            raise BackendError("not enough data to read header length")
        header_len = struct.unpack("!H", header_len_buf)[0]
        header_buf = await self.reader.read(header_len)
        if len(header_buf) < header_len:
            raise BackendError("not enough data to read header data")

        header = rpc_pb2.Header()
        header.ParseFromString(header_buf)

        body_len = header.size
        if body_len:
            body = await self.reader.read(body_len)
            if len(body) < body_len:
                raise BackendError("not enough data to read body data")
        else:
            body = None

        log.debug(f"protobuf receiving data: service {header.service_id} method {header.method_id} token {header.token} status {header.status} size {header.size}")

        # this is a response to a request from us
        if header.service_id == self._RESPONSE_SERVICE_ID:
            if header.token in self._token_callbacks:
                callback = self._token_callbacks[header.token]
                await callback(header, body)
                del self._token_callbacks[header.token]
            else:
                log.warning("unexpected response received", str(header))

        # server requesting something from us
        try:
            callback = self._exported_services_map[header.service_id][header.method_id]
            await callback(header, body)
        except Exception as e:
            log.warning("failed to run service for received header", str(header), e)

    async def logon(self):
        request = authentication_service_pb2.LogonRequest()
        # request.program = "App"  # Battle.net Desktop App, using this would logout of running Battle.net App
        request.program = "BSAp"  # Battle.net Mobile App
        request.platform = "Win"
        request.locale = "enUS"
        request.version = "9166"
        request.application_version = 1
        request.public_computer = False
        request.disconnect_on_cookie_fail = False
        request.allow_logon_queue_notifications = True
        request.cached_web_credentials = str.encode(utils.dict_from_cookiejar(self._authentication_client.auth_data.cookie_jar)["BA-tassadar"])
        # request.user_agent = "Battle.net/1.8.2.8839"

        await self._send_message(self._AUTHENTICATION_SERVER_SERVICE, 1, request)

    async def connect(self):
        self._set_backend_server_host(self._authentication_client.auth_data.region)

        self.reader, self.writer = await asyncio.open_connection(
            self._BACKEND_SERVER_HOST, self._BACKEND_SERVER_PORT, ssl=True
        )

        request = connection_service_pb2.ConnectRequest()
        request.bind_request.imported_service_hash.extend([fnv1a_32(bytes(s, "UTF-8")) for s in self._imported_services])
        request.bind_request.exported_service.extend([connection_service_pb2.BoundService(hash=fnv1a_32(bytes(s.name, "UTF-8")), id=s.id ) for s in self._exported_services])

        await self._send_message(self._CONNECTION_SERVICE, 1, request, self._on_connection__connect_response)

        asyncio.create_task(self._watch_receive_message())

    async def disconnect(self):
        log.info("disconnected from battle.net")
        if self.writer:
            self.writer.close()
        self.writer = None
        self.reader = None
        self.authenticated = False

    async def fetch_friend_battle_tag(self, entity_id, future: 'asyncio.Future[AccountInfo]'):
        request = presence_service_pb2.QueryRequest()
        request.entity_id.high = entity_id.high
        request.entity_id.low = entity_id.low
        for i in [4]:  # for possible values see self.AccountInfo
            key = request.key.add()
            key.program = 0x424e  # hex code for "BN"
            key.group = 1  # account
            key.field = i

        await self._send_message(self._PRESENCE_SERVICE, 4, request, functools.partial(self._on_presence__query_account, future))

    async def fetch_friend_presence_account_details(self, entity_id, future: 'asyncio.Future[AccountInfo]'):
        request = presence_service_pb2.QueryRequest()
        request.entity_id.high = entity_id.high
        request.entity_id.low = entity_id.low
        for i in [3]:  # for possible values see self.AccountInfo
            key = request.key.add()
            key.program = 0x424e  # hex code for "BN"
            key.group = 1  # account
            key.field = i

        await self._send_message(self._PRESENCE_SERVICE, 4, request, functools.partial(self._on_presence__query_account, future))

    async def fetch_friend_presence_game_account_details(self, entity_id, future: 'asyncio.Future[GameAccountInfo]'):
        request = presence_service_pb2.QueryRequest()
        request.entity_id.high = entity_id.high
        request.entity_id.low = entity_id.low
        for i in [3, 10]:  # for possible values see self.GameAccountInfo
            key = request.key.add()
            key.program = 0x424e  # hex code for "BN"
            key.group = 2  # game account
            key.field = i

        await self._send_message(self._PRESENCE_SERVICE, 4, request, functools.partial(self._on_presence__query_game_account, future))

    async def fetch_friends_list(self, future: 'asyncio.Future[List[friends_types_pb2.Friend]]'):
        request = friends_service_pb2.SubscribeToFriendsRequest()
        request.object_id = self._next_object()

        await self._send_message(self._FRIENDS_SERVICE, 1, request, functools.partial(self._on_friends__subscribe_to_friends, future))
