import os
import asyncio
import json
from unittest.mock import Mock

import pytest
from galaxy.api.types import GameTime

from tests.async_mock import AsyncMock
from src.definitions import Blizzard, ConfigGameInfo
from src.parsers import ConfigParser

# pytest-asyncio: all test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio

OW_ID = '5272175'
NO_GAME_TIME = GameTime(OW_ID, None, None)


@pytest.fixture()
def ow_player_data_response_public():
    return json.loads("""{"username":"public","level":1307,"portrait":"https://d15f34w2p8l1cc.cloudfront.net/overwatch/182501bf4c655b69acc9ad25cf82fa0f2a8024a8d3409b09d309eab4c2239e63.png","endorsement":{"sportsmanship":{"value":0.31,"rate":31},"shotcaller":{"value":0.16,"rate":16},"teammate":{"value":0.53,"rate":53},"level":null,"frame":"https://static.playoverwatch.com/svg/icons/endorsement-frames-3c9292c49d.svg#_3","icon":"data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjQwIiB3aWR0aD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxjaXJjbGUgcj0iMTUuOTE1NDk0MzA5MTg5NTQiIGZpbGw9IiMyYTJiMmUiIHN0cm9rZS1kYXNoYXJyYXk9IjE2IDg0IiBzdHJva2UtZGFzaG9mZnNldD0iMjUiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlPSIjZjE5NTEyIiBjeD0iNTAlIiBjeT0iNTAlIj48L2NpcmNsZT48Y2lyY2xlIHI9IjE1LjkxNTQ5NDMwOTE4OTU0IiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLWRhc2hhcnJheT0iNTMgNDciIHN0cm9rZS1kYXNob2Zmc2V0PSIxMDkiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlPSIjYzgxYWY1IiBjeD0iNTAlIiBjeT0iNTAlIj48L2NpcmNsZT48Y2lyY2xlIHI9IjE1LjkxNTQ5NDMwOTE4OTU0IiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLWRhc2hhcnJheT0iMzEgNjkiIHN0cm9rZS1kYXNob2Zmc2V0PSI1NiIgc3Ryb2tlLXdpZHRoPSIzIiBzdHJva2U9IiM0MGNlNDQiIGN4PSI1MCUiIGN5PSI1MCUiPjwvY2lyY2xlPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBkeT0iLjNlbSIgZm9udC1mYW1pbHk9ImNlbnR1cnkgZ290aGljLGFyaWFsLHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSIzMDAiIGZvbnQtc2l6ZT0iMTYiIHN0cm9rZT0iI2Y2ZjZmNiIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSIjZjZmNmY2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5OYU48L3RleHQ+PC9zdmc+"},"private":false,"games":{"quickplay":{"won":2449},"competitive":{"won":19,"lost":21,"draw":1,"played":41,"win_rate":47.5}},"playtime":{"quickplay":"628:53:21","competitive":"07:29:56"},"competitive":{"tank":{"rank":null,"rank_img":null},"damage":{"rank":null,"rank_img":null},"support":{"rank":null,"rank_img":null}},"levelFrame":"https://d15f34w2p8l1cc.cloudfront.net/overwatch/5ab5c29e0e1e33f338ae9afc37f51917b151016aef42d10d361baac3e0965df1.png","star":"https://d15f34w2p8l1cc.cloudfront.net/overwatch/1858704e180db3578839aefdb83b89054f380fbb3d4c46b3ee12d34ed8af8712.png"}""")


@pytest.fixture()
def ow_player_data_response_private():
    return json.loads("""{"username":"private","level":452,"portrait":"https://d15f34w2p8l1cc.cloudfront.net/overwatch/e9510e804e002aa86633aeebbd158173e3432c32380a063b03f06f8f4aa401ca.png","endorsement":{"sportsmanship":{"value":0.17,"rate":17},"shotcaller":{"value":0.2,"rate":20},"teammate":{"value":0.63,"rate":63},"level":null,"frame":"https://static.playoverwatch.com/svg/icons/endorsement-frames-3c9292c49d.svg#_3","icon":"data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjQwIiB3aWR0aD0iNDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxjaXJjbGUgcj0iMTUuOTE1NDk0MzA5MTg5NTQiIGZpbGw9IiMyYTJiMmUiIHN0cm9rZS1kYXNoYXJyYXk9IjIwIDgwIiBzdHJva2UtZGFzaG9mZnNldD0iMjUiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlPSIjZjE5NTEyIiBjeD0iNTAlIiBjeT0iNTAlIj48L2NpcmNsZT48Y2lyY2xlIHI9IjE1LjkxNTQ5NDMwOTE4OTU0IiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLWRhc2hhcnJheT0iNjMgMzciIHN0cm9rZS1kYXNob2Zmc2V0PSIxMDUiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlPSIjYzgxYWY1IiBjeD0iNTAlIiBjeT0iNTAlIj48L2NpcmNsZT48Y2lyY2xlIHI9IjE1LjkxNTQ5NDMwOTE4OTU0IiBmaWxsPSJ0cmFuc3BhcmVudCIgc3Ryb2tlLWRhc2hhcnJheT0iMTcgODMiIHN0cm9rZS1kYXNob2Zmc2V0PSI0MiIgc3Ryb2tlLXdpZHRoPSIzIiBzdHJva2U9IiM0MGNlNDQiIGN4PSI1MCUiIGN5PSI1MCUiPjwvY2lyY2xlPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBkeT0iLjNlbSIgZm9udC1mYW1pbHk9ImNlbnR1cnkgZ290aGljLGFyaWFsLHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSIzMDAiIGZvbnQtc2l6ZT0iMTYiIHN0cm9rZT0iI2Y2ZjZmNiIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSIjZjZmNmY2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5OYU48L3RleHQ+PC9zdmc+"},"private":true,"games":{"quickplay":{"won":null},"competitive":{"won":null,"lost":null,"draw":0,"played":null,"win_rate":null}},"playtime":{},"competitive":{"tank":{"rank":null,"rank_img":null},"damage":{"rank":null,"rank_img":null},"support":{"rank":null,"rank_img":null}},"levelFrame":"https://d15f34w2p8l1cc.cloudfront.net/overwatch/3fdfdd16c34ab7cdc9b7be3c04197e900928b368285ce639c1d3e1c0619eea6d.png","star":"https://d15f34w2p8l1cc.cloudfront.net/overwatch/bc80149bbd78d2f940984712485bce23ddaa6f2bd0edd1c0494464ef55251eef.png"}""")


@pytest.fixture
def ow_player_data_response_not_found():
    return json.loads("""{"message":"Error: Profile not found"}""")


async def test_overwatch_private_profile(pg, backend_mock, ow_player_data_response_private):
    backend_mock.get_ow_player_data.return_value = ow_player_data_response_private

    ctx = await pg.prepare_game_times_context([OW_ID])
    assert await pg.get_game_time(OW_ID, ctx) == NO_GAME_TIME


async def test_overwatch_missing_profile(pg, backend_mock, ow_player_data_response_not_found):
    backend_mock.get_ow_player_data.return_value = ow_player_data_response_not_found

    ctx = await pg.prepare_game_times_context([OW_ID])
    assert await pg.get_game_time(OW_ID, ctx) == NO_GAME_TIME


@pytest.mark.parametrize("playtime,minutes", [
    ({'quickplay': "628:53:21", 'competitive': "07:29:56"}, 628*60+53),
    ({'quickplay': "628:53:21", 'competitive': "0:00"}, 628*60+53),
    ({'quickplay': "0:00", 'competitive': "0:00"}, 0),
    ({'quickplay': None, 'competitive': None}, 0),
])
async def test_overwatch_public_profile(
    playtime, minutes,
    pg, backend_mock, ow_player_data_response_public
):
    ow_player_data_response_public['playtime'] = playtime
    backend_mock.get_ow_player_data.return_value = ow_player_data_response_public

    ctx = await pg.prepare_game_times_context([OW_ID])
    result = await pg.get_game_time(OW_ID, ctx)
    assert result == GameTime(OW_ID, minutes, None)


@pytest.mark.asyncio
async def test_last_played_when_unknown_game_in_config(pg, config_parser):
    game = Blizzard['diablo3']
    unknown_game_uid = 'unknown_game'
    with pytest.raises(KeyError):
        assert Blizzard[unknown_game_uid]  # test precondition

    config_parser.games = [
        ConfigGameInfo(unknown_game_uid, 'mock', '111111111'),
        ConfigGameInfo(game.uid, 'diablo3_enus', '1441712029')
    ]

    ctx = await pg.prepare_game_times_context([game.blizzard_id])
    result = await pg.get_game_time(game.blizzard_id, ctx)
    assert result.game_id == game.blizzard_id
    assert result.last_played_time == 1441712029

async def test_last_played_time(pg, config_data):
    pg.local_client.config_parser = ConfigParser(config_data)

    ctx = await pg.prepare_game_times_context(["21298", "1214607983"])

    result = await pg.get_game_time("21298", ctx)
    assert result == GameTime("21298", None, None)

    result = await pg.get_game_time("1214607983", ctx)
    assert result == GameTime("1214607983", None, 1441712029)
