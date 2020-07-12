import asyncio
import logging as log
import json


class SocialFeatures(object):
    def __init__(self, _bnet_client):
        self.bnet_client = _bnet_client
        self._friends = {}
        self._friends_presence = {}

    async def get_friends(self):
        _friends_future = asyncio.get_running_loop().create_future()
        await self.bnet_client.fetch_friends_list(_friends_future)
        await _friends_future

        self._friends = {}
        for friend in _friends_future.result():
            _friend_battle_tag_future = asyncio.get_running_loop().create_future()
            await self.bnet_client.fetch_friend_battle_tag(friend.id, _friend_battle_tag_future)
            await _friend_battle_tag_future

            friend.battle_tag = _friend_battle_tag_future.result()["battle_tag"]
            self._friends[str(friend.id.low)] = friend

        log.debug(f"fetched {len(self._friends)} friends")

        return self._friends

    async def get_friend_presence(self, user_id):
        _friend_presence_future = asyncio.get_running_loop().create_future()
        await self.bnet_client.fetch_friend_presence_account_details(self._friends[user_id].id, _friend_presence_future)
        await _friend_presence_future

        self._friends_presence[user_id] = _friend_presence_future.result()

        log.debug(f"fetched friend presence [id = user_id]: {json.dumps(self._friends_presence[user_id], default=str)}")

        return self._friends_presence[user_id]
