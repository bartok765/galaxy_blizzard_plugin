import socket
import ssl
from fnvhash import fnv1a_32
# from bnet.protocol import protocol_pb2
# from bnet.protocol.authentication import authentication_pb2
# from bnet.protocol.channel_extracted import channel_extracted_pb2
# from bnet.protocol.connection import connection_pb2
# from bnet.protocol.friends import friends_pb2
# from bnet.protocol.presence import presence_pb2
from bnet import connection_service_pb2, rpc_pb2, friends_service_pb2, authentication_service_pb2, presence_service_pb2, presence_types_pb2
import struct
import functools
import logging as log
from requests import utils
from datetime import datetime


class BNetClient:
    def __init__(self, authentication_client):
        self._authentication_client = authentication_client
        self._BACKEND_SERVER_HOST = None
        self._BACKEND_SERVER_PORT = 1119

        self._AUTHENTICATION_SERVER_SERVICE = "bnet.protocol.authentication.AuthenticationServer"
        self._AUTHENTICATION_CLIENT_SERVICE = "bnet.protocol.authentication.AuthenticationClient"
        self._PRESENCE_SERVICE = "bnet.protocol.presence.PresenceService"
        self._FRIENDS_SERVICE = "bnet.protocol.friends.FriendsService"

        self._RESPONSE_SERVICE = "response"
        self._RESPONSE_SERVICE_ID = 254
        self._CONNECTION_SERVICE = "bnet.protocol.connection.ConnectionService"
        self._CONNECTION_SERVICE_ID = 0

        self._imported_services = (
            self._AUTHENTICATION_SERVER_SERVICE,
            self._PRESENCE_SERVICE,
            self._FRIENDS_SERVICE,
        )

        self._imported_services_map = {
            self._RESPONSE_SERVICE: self._RESPONSE_SERVICE_ID,
            self._CONNECTION_SERVICE: self._CONNECTION_SERVICE_ID
        }
        self._exported_services = (
            self.ExportedService(1, "bnet.protocol.authentication.AuthenticationClient"),
            self.ExportedService(5, "bnet.protocol.friends.FriendsNotify"))

        self._exported_services_map = {}

        self._object = 1
        self._token = 0
        self._callbacks = {}
        self._account_id = None
        self._game_account_id = None
        self.connection = None

        self.connect_callback = None

    class ExportedService:
        def __init__(self, id, name):
            self.name = name
            self.id = id
            self.hash = fnv1a_32(bytes(name, "UTF-8"))

    def _next_object(self):
        self._object += 1
        return self._object

    def _next_token(self):
        self._token += 1
        return self._token

    def _set_backend_server_host(self, region):
        self._BACKEND_SERVER_HOST = "{}.actual.battle.net".format(region)

    def _send_request(self, service_name, method_id, body, callback=None):
        # header = protocol_pb2.Header()
        header = rpc_pb2.Header()

        service_id = self._imported_services_map[service_name]
        header.service_id = service_id

        if service_id != self._RESPONSE_SERVICE_ID:
            header.method_id = method_id
            header.token = self._next_token()
        else:
            header.method_id = 0
            header.token = method_id

        header.size = body.ByteSize()

        if callback:
            self._callbacks[header.token] = callback

        log.debug(f"protobuf request: {service_name}::{method_id} token {header.token}")

        self.connection.send(struct.pack("!H", header.ByteSize()))
        self.connection.send(header.SerializeToString())
        self.connection.send(body.SerializeToString())

    def _on_query_game_account_info_response(self, entity_id, account_info, callback, header, body):
        if not body:
            callback(False, entity_id, account_info)
            return

        # packet = presence_pb2.QueryResponse()
        packet = presence_service_pb2.QueryResponse()
        packet.ParseFromString(body)
        # log.debug(f"fetched query_game_account_info_response packet: {packet}")

        for f in packet.field:
            if f.key.field == 1 and f.key.group == 2:
                account_info["game_account_is_online"] = f.value.bool_value
            if f.key.field == 3 and f.key.group == 2:
                account_info["program_id"] = f.value.fourcc_value  # e.g. "App" or "BSAp"
            elif f.key.field == 8 and f.key.group == 2:
                rich_presence = presence_types_pb2.RichPresence()
                rich_presence.ParseFromString(f.value.message_value)
                account_info["rich_presence"] = rich_presence

        callback(True, entity_id, account_info)

    def _on_query_account_info_response(self, entity_id, query_game_account_info, callback, header, body):
        if not body:
            callback(False, entity_id, {})
            return

        # packet = presence_pb2.QueryResponse()
        packet = presence_service_pb2.QueryResponse()
        packet.ParseFromString(body)

        # log.debug(f"fetched query_account_info_response packet: {packet}")

        account_info = {}

        for f in packet.field:
            if f.key.field == 1 and f.key.group == 1:
                account_info["full_name"] = f.value.string_value.encode('utf-8')  # e.g. "Firstname Lastname"
            elif f.key.field == 3 and f.key.group == 1 and "game_account" not in account_info:
                account_info["game_account"] = f.value.entityid_value  # e.g. high: 144115197778542960 low: 131237370
            elif f.key.field == 4 and f.key.group == 1:
                account_info["battle_tag"] = f.value.string_value  # e.g. "Username#1234"
            elif f.key.field == 6 and f.key.group == 1:
                account_info["last_online"] = datetime.fromtimestamp(f.value.int_value/1000/1000)  # e.g. 1584194739362351 (microseconds timestamp)
            elif f.key.field == 7 and f.key.group == 1:
                account_info["is_away"] = f.value.bool_value
            elif f.key.field == 11 and f.key.group == 1:
                account_info["is_busy"] = f.value.bool_value

        if not query_game_account_info or "game_account" not in account_info:
            callback(True, entity_id, account_info)
            return

        # request = presence_pb2.QueryRequest()
        request = presence_service_pb2.QueryRequest()
        request.entity_id.high = account_info["game_account"].high
        request.entity_id.low = account_info["game_account"].low

        for i in [1, 3, 8]:  # 1 - is_online, 3 - program_id, 4 - last_online???, 5 - battle_tag, 7 - ???, 8 - rich_presence, 9 - ???, 10 - is_online???, 11 - last_online???
            key = request.key.add()
            key.program = 0x424e
            key.group = 2  # 2 game account
            key.field = i

        # request with key.field = 1 (is online) works for all not-offline friends and always returns true (even if user is away)
        # request with key.field = 3 (program_id) works for all not-offline friends and returns e.g. BSAp
        # request with key.field = 4 (last_online???) returns e.g. 1584194739362351
        # request with key.field = 7 (???) returns e.g. high: 72057594037927936 low: 101974425
        # request with key.field = 8 (rich_presence) only returns when user is in-game
        # request with key.field = 9 (???) return e.g. 1584228809551117

        self._send_request(self._PRESENCE_SERVICE, 4, request, functools.partial(self._on_query_game_account_info_response, entity_id, account_info, callback))

    def _on_subscribe_to_presence_response(self, callback, header, body):
        log.info(f"fetched presence_response header: {header} -- body: {body}")
        if not body:
            callback(False, 0, [])
            return

        packet = body
        # packet = presence_pb2.SubscribeResponse()
        packet.ParseFromString(body)
        log.info(f"fetched presence_response packet: {packet}")
        callback(True, 0, packet)

    def _on_subscribe_to_friends_response(self, callback, header, body):
        if not body:
            callback(False, [])
            return

        # packet = channel_extracted_pb2.SubscribeToFriendsResponse()
        packet = friends_service_pb2.SubscribeToFriendsResponse()
        packet.ParseFromString(body)
        # log.info(f"fetched friends_response packet: {packet}")
        callback(True, packet.friends)

    def _on_select_game_account(self, header, body):
        self.connect_callback(True)

    def _on_logon_result(self, header, body):
        if header.status != 0:
            self.connect_callback(False)
            return

        # packet = authentication_pb2.LogonResult()
        packet = authentication_service_pb2.LogonResult()
        packet.ParseFromString(body)

        self._account_id = packet.account
        self._game_account_id = packet.game_account[0]

        # request = authentication_service_pb2.SelectGameAccountRequest()
        # request.game_account.high = self._game_account_id.high
        # request.game_account.low = self._game_account_id.low
        #
        # self._send_request(self._AUTHENTICATION_SERVER_SERVICE, 6, request, self._on_select_game_account)

        self._send_request(self._AUTHENTICATION_SERVER_SERVICE, 4, self._game_account_id, self._on_select_game_account)

    # def _on_logon_response(self, header, body):
    #     if header.status != 0:
    #         self.connect_callback(False)

    def _send_logon_request(self):
        # request = authentication_pb2.LogonRequest()
        request = authentication_service_pb2.LogonRequest()
        #request.program = "App"
        request.program = "BSAp"  # login in as mobile
        request.platform = "Win"

        request.locale = "enUS"
        request.version = "9166"
        request.application_version = 1
        request.public_computer = False
        request.disconnect_on_cookie_fail = False
        request.allow_logon_queue_notifications = True
        request.cached_web_credentials = str.encode(utils.dict_from_cookiejar(self._authentication_client.auth_data.cookie_jar)["BA-tassadar"])

        self._send_request(self._AUTHENTICATION_SERVER_SERVICE, 1, request)

    def _on_connect_response(self, header, body):
        # response = connection_pb2.ConnectResponse()
        response = connection_service_pb2.ConnectResponse()
        response.ParseFromString(body)

        self._imported_services_map.update(zip(self._imported_services, response.bind_response.imported_service_id))
        self._exported_services_map[1] = {5: self._on_logon_result}

        self._send_logon_request()

    async def connect(self, callback):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)

        self._set_backend_server_host(self._authentication_client.auth_data.region)
        connection = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1)
        connection.connect((self._BACKEND_SERVER_HOST, self._BACKEND_SERVER_PORT))
        connection.do_handshake()

        self.connect_callback = callback
        self.connection = connection

        # request = connection_pb2.ConnectRequest()
        request = connection_service_pb2.ConnectRequest()
        request.bind_request.imported_service_hash.extend([fnv1a_32(bytes(s, "UTF-8")) for s in self._imported_services])
        # request.bind_request.exported_service.extend([connection_pb2.BoundService(hash=fnv1a_32(bytes(s.name, "UTF-8")), id=s.id ) for s in self._exported_services])
        request.bind_request.exported_service.extend([connection_service_pb2.BoundService(hash=fnv1a_32(bytes(s.name, "UTF-8")), id=s.id ) for s in self._exported_services])

        self._send_request(self._CONNECTION_SERVICE, 1, request, self._on_connect_response)

    async def process_request(self):
        header_len_buf = self.connection.recv(2)
        if len(header_len_buf) < 2:
            raise Exception("not enough data to read header length")
        header_len = struct.unpack("!H", header_len_buf)[0]
        header_buf = self.connection.recv(header_len)
        if len(header_buf) < header_len:
            raise Exception("not enough data to read header data")

        # header = protocol_pb2.Header()
        header = rpc_pb2.Header()
        header.ParseFromString(header_buf)

        body_len = header.size
        if body_len:
            body = self.connection.recv(body_len)
            if len(body) < body_len:
                raise Exception("not enough data to read body data")
        else:
            body = None

        log.debug(f"protobuf response header: token {header.token} status {header.status} size {header.size}")

        if header.service_id == self._RESPONSE_SERVICE_ID:
            if header.token in self._callbacks:
                callback = self._callbacks[header.token]
                callback(header, body)
                del self._callbacks[header.token]
            else:
                log.debug("unexpected response received", str(header))

        try:
            self._exported_services_map[header.service_id][header.method_id](header, body)
        except Exception as e:
            log.debug("failed to run service for received header", str(header), e)

    def query_account_info(self, entity_id, callback, query_game_account_info=True):
        # request = presence_pb2.QueryRequest()
        request = presence_service_pb2.QueryRequest()
        request.entity_id.high = entity_id.high
        request.entity_id.low = entity_id.low
        # 1 - full_name, 3 - game_account, 4 - battle_tag, 6 - last_online, 7 - is_away???, 8 - ???, 11 - is_busy???
        for i in [3, 4, 6, 7, 11]:  # 1, 3, 4, 6, 7, 11
            key = request.key.add()
            key.program = 0x424e
            key.group = 1  # account
            key.field = i

        # request with key.field = 1 (full_name) only works for RealId friends, others will return with header.status = 3 and empty body
        # request with key.field = 4 (battle_tag) works for all friends
        # request with key.field = 3 (game_account) works for all friends, but is only returned when friend is not offline!
        #   key.field = 3 (game_account) can be returned multiple times!
        #   e.g. id 436369611 (GamerSide#21802) has 2, id 129118839 (ExPliciT#21888) has 3)
        #   seems to be for different programs, where user is logged in (e.g. PC, Mobile etc.)
        # request with key.field = 6 (last_online) works for all friends
        # request with key.field = 7 (is_away) always returns false
        # request with key.field = 8 (???) return e.g. 1583607638026991
        # request with key.field = 11 (is_busy) always returns false

        self._send_request(self._PRESENCE_SERVICE, 4, request, functools.partial(self._on_query_account_info_response, entity_id, query_game_account_info, callback))

    def fetch_friend_presence(self, game_account_id, friend_id, callback):
        # request = presence_pb2.SubscribeRequest()
        request = presence_service_pb2.SubscribeRequest()
        request.agent_id.high = self._account_id.high
        request.agent_id.low = self._account_id.low
        request.entity_id.high = game_account_id.high
        request.entity_id.low = game_account_id.low
        request.object_id = self._next_object()

        self._send_request(self._PRESENCE_SERVICE, 1, request, functools.partial(self._on_subscribe_to_presence_response, callback))

    def fetch_friends_list(self, callback):
        # request = friends_pb2.SubscribeToFriendsRequest()
        request = friends_service_pb2.SubscribeToFriendsRequest()
        request.agent_id.high = self._account_id.high
        request.agent_id.low = self._account_id.low
        request.object_id = self._next_object()

        self._send_request(self._FRIENDS_SERVICE, 1, request, functools.partial(self._on_subscribe_to_friends_response, callback))
