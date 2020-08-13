import asyncio
import json
import logging as log
from typing import Dict, List

from definitions import EntityId, Friend, FriendPresence


class SocialFeatures(object):
    def __init__(self, _bnet_client):
        self.bnet_client = _bnet_client
        self._friends: Dict[str, Friend] = {}

    async def get_friends(self) -> Dict[str, Friend]:
        _friends_future = asyncio.get_running_loop().create_future()
        await self.bnet_client.fetch_friends_list(_friends_future)
        await asyncio.wait_for(_friends_future, timeout=2)

        self._friends = {}
        for friend in _friends_future.result():
            _friend_battle_tag_future = asyncio.get_running_loop().create_future()
            await self.bnet_client.fetch_friend_battle_tag(friend.id, _friend_battle_tag_future)
            await asyncio.wait_for(_friend_battle_tag_future, timeout=2)

            _friend = Friend(EntityId(friend.id.high, friend.id.low), _friend_battle_tag_future.result().battle_tag)
            self._friends[_friend.uid] = _friend

        log.debug(f"fetched {len(self._friends)} friends: {json.dumps(self._friends, default=str)}")

        return self._friends

    async def get_friend_presences(self, user_id) -> List[FriendPresence]:
        if user_id not in self._friends:
            return []

        _account_future = asyncio.get_running_loop().create_future()
        await self.bnet_client.fetch_friend_presence_account_details(self._friends[user_id].entity_id, _account_future)
        await asyncio.wait_for(_account_future, timeout=2)

        _friend_presences = []
        for game_account_id in _account_future.result().game_account_ids:
            _game_account_future = asyncio.get_running_loop().create_future()
            await self.bnet_client.fetch_friend_presence_game_account_details(game_account_id, _game_account_future)
            await asyncio.wait_for(_game_account_future, timeout=2)

            _friend_presence = FriendPresence(EntityId(game_account_id.high, game_account_id.low), _game_account_future.result().is_away, _game_account_future.result().program)
            _friend_presences.append(_friend_presence)

        log.debug(f"fetched friend presence ({user_id}): {json.dumps(_friend_presences, default=str)}")

        return _friend_presences
