import logging as log
import json


class SocialFeatures(object):
    def __init__(self, _bnet_client):
        self.bnet_client = _bnet_client
        self._friends = None
        self._friends_battle_tags = {}
        self._friends_presence = {}

    def fetch_friends_list_callback(self, success, friends):
        self._friends = {}
        if not success:
            log.error("failed to fetch friend list")
            return
        # log.debug(f"fetched friend list: {friends}")
        for friend in friends:
            self._friends[str(friend.id.low)] = friend

    def fetch_friend_battle_tag_callback(self, success, entity_id, presence):
        self._friends_battle_tags[str(entity_id.low)] = presence["battle_tag"]

    def fetch_friend_presence_callback(self, success, entity_id, presence):
        log.debug(f"fetched friend presence [id = {str(entity_id.low)}]: {json.dumps(presence, default=str)}")
        self._friends_presence[str(entity_id.low)] = presence

    async def get_friends(self):
        self._friends = None
        self.bnet_client.fetch_friends_list(self.fetch_friends_list_callback)
        while self._friends is None:
            await self.bnet_client.receive_message()
        return self._friends

    async def get_friend_battle_tag(self, user_id):
        self._friends_battle_tags[user_id] = None
        self.bnet_client.fetch_friend_battle_tag(self._friends[user_id].id, self.fetch_friend_battle_tag_callback)
        while self._friends_battle_tags[user_id] is None:
            await self.bnet_client.receive_message()
        return self._friends_battle_tags[user_id]

    async def get_friend_presence(self, user_id):
        self._friends_presence[user_id] = None
        self.bnet_client.fetch_friend_presence_account_details(self._friends[user_id].id, self.fetch_friend_presence_callback)
        while self._friends_presence[user_id] is None:
            await self.bnet_client.receive_message()
        return self._friends_presence[user_id]
