import logging as log
from battlenet import BNetClient


class SocialFeatures(object):
    def __init__(self, _authentication_client):
        self._authentication_client = _authentication_client
        self.bnet_client = BNetClient(self._authentication_client)
        self.friends_id = None

    def query_account_info_callback(self, entity_id, success, account_info):
        return

    def fetch_friend_list_callback(self, success, friends):
        if not success:
            log.error("Failed to fetch friend list")
            return
        self.friends_id = friends

    def connect_callback(self, success):
        if not success:
            log.error("failed to connect to battle.net")
            return
        self.bnet_client.fetch_friend_list(self.fetch_friend_list_callback)

    async def get_friends(self):
        self.friends_id = None
        await self.bnet_client.connect(self.connect_callback)
        while self.friends_id is None:
            await self.bnet_client.process_request()
        return self.friends_id
