import logging as log
from bnet_client import BNetClient


class SocialFeatures(object):
    def __init__(self, _authentication_client):
        self._authentication_client = _authentication_client
        self.bnet_client = BNetClient(self._authentication_client)
        self._friends = None
        self._friends_presence = {}

    def fetch_friends_list_callback(self, success, friends):
        self._friends = {}
        if not success:
            log.error("failed to fetch friend list")
            return
        # log.debug(f"fetched friend list: {friends}")
        for friend in friends:
            self._friends[str(friend.id.low)] = friend

    def fetch_friend_presence_callback(self, success, entity_id, presence):
        log.debug(f"fetched friend presence [id = {str(entity_id.low)}]: {presence}")
        self._friends_presence[str(entity_id.low)] = presence
        return

    def connect_callback(self, success):
        if not success:
            log.error("failed to connect to battle.net")
            return
        self.bnet_client.fetch_friends_list(self.fetch_friends_list_callback)

    async def get_friends(self):
        self._friends = None
        # if self.bnet_client.connection is None:
        #     await self.bnet_client.connect(self.connect_callback)
        await self.bnet_client.connect(self.connect_callback)
        while self._friends is None:
            await self.bnet_client.process_request()
        return self._friends

    async def get_friend_presence(self, user_id):
        self._friends_presence[user_id] = None
        self.bnet_client.query_account_info(self._friends[user_id].id, self.fetch_friend_presence_callback)
        while self._friends_presence[user_id] is None:
            await self.bnet_client.process_request()
        return self._friends_presence[user_id]
