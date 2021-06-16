import pytest

from galaxy.api.types import Game, LicenseInfo
from galaxy.api.consts import LicenseType

from definitions import Blizzard
from tests.website_mocks import backend_owned_games, backend_no_classics, backend_classic_games


@pytest.fixture
def result_owned_games():
    vals = [
        Blizzard['wow'],
        Blizzard['odin'],
        Blizzard['s1'],
        Blizzard['s2'],
        Blizzard['prometheus'],
        Blizzard['diablo3'],
        Blizzard['hs_beta'],
        Blizzard['heroes'],
        Blizzard['wow_classic']
    ]

    return [
        Game(game.uid, game.name, None, LicenseInfo(LicenseType.SinglePurchase))
        for game in vals
    ]


@pytest.fixture
def result_classic_games():
    return [
        Game('d2', 'Diablo® II', None, LicenseInfo(LicenseType.SinglePurchase)),
    ]


@pytest.mark.asyncio
async def test_owned_games(pg, backend_mock, backend_owned_games, backend_no_classics, result_owned_games):
    backend_mock.get_owned_games.return_value = backend_owned_games
    backend_mock.get_owned_classic_games.return_value = backend_no_classics

    result = await pg.get_owned_games()
    assert sorted(result, key=lambda x: x.game_id) == sorted(result_owned_games, key=lambda x: x.game_id)


@pytest.mark.parametrize("game_account_status", [
    "NEW_STATUS",
    True,
    None,
    0
])
@pytest.mark.asyncio
async def test_owned_games_with_unknown_licenses(pg, backend_mock, backend_owned_games, result_owned_games, game_account_status):
    backend_owned_games["gameAccounts"][1]['gameAccountStatus'] = game_account_status
    result_owned_games[1] = Game("odin", "Call of Duty: Modern Warfare", None, LicenseInfo(LicenseType.Unknown))
    backend_mock.get_owned_games.return_value = backend_owned_games
    backend_mock.get_owned_classic_games.return_value = {"classicGames": []}

    result = await pg.get_owned_games()

    assert sorted(result, key=lambda x: x.game_id) == sorted(result_owned_games, key=lambda x: x.game_id)


@pytest.mark.asyncio
async def test_owned_games_without_account_status(pg, backend_mock, backend_owned_games, result_owned_games):
    backend_owned_games["gameAccounts"][1].pop('gameAccountStatus')
    result_owned_games[1] = Game("odin", "Call of Duty: Modern Warfare", None, LicenseInfo(LicenseType.Unknown))
    backend_mock.get_owned_games.return_value = backend_owned_games
    backend_mock.get_owned_classic_games.return_value = {"classicGames": []}

    result = await pg.get_owned_games()

    assert sorted(result, key=lambda x: x.game_id) == sorted(result_owned_games, key=lambda x: x.game_id)


@pytest.mark.asyncio
async def test_integration(
    pg, backend_mock, backend_owned_games, backend_classic_games, result_owned_games, result_classic_games
):
    backend_mock.get_owned_games.return_value = backend_owned_games
    backend_mock.get_owned_classic_games.return_value = backend_classic_games

    result = await pg.get_owned_games()
    assert sorted(result, key=lambda x: x.game_id) == sorted(result_owned_games + result_classic_games, key=lambda x: x.game_id)

