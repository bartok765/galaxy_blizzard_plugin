import os
import asyncio
from galaxy.api.types import GameTime

game_time_empty = GameTime("5272175", None, None)

def test_overwatch_public_profile(create_authenticated_plugin):
    loop = asyncio.get_event_loop()
    pg = create_authenticated_plugin()

    os.environ['TEST_BLIZZARD_BATTLETAG'] = 'public'
    result = loop.run_until_complete(pg.get_game_time("5272175", None))
    os.environ.pop('TEST_BLIZZARD_BATTLETAG')

    # playtime set in website_mock.py is 628:53:21 (hh:mm:ss)
    assert result == GameTime("5272175", 628*60+53, None)

def test_overwatch_private_profile(create_authenticated_plugin):
    loop = asyncio.get_event_loop()
    pg = create_authenticated_plugin()

    os.environ['TEST_BLIZZARD_BATTLETAG'] = 'private'
    result = loop.run_until_complete(pg.get_game_time("5272175", None))
    os.environ.pop('TEST_BLIZZARD_BATTLETAG')

    assert result == game_time_empty

def test_overwatch_missing_profile(create_authenticated_plugin):
    loop = asyncio.get_event_loop()
    pg = create_authenticated_plugin()

    os.environ['TEST_BLIZZARD_BATTLETAG'] = 'unknown'
    result = loop.run_until_complete(pg.get_game_time("5272175", None))
    os.environ.pop('TEST_BLIZZARD_BATTLETAG')

    assert result == game_time_empty
