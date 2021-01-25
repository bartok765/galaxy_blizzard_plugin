import asyncio
import pytest
import json

from galaxy.api.types import Game, LicenseInfo, LocalGame
from galaxy.api.consts import LicenseType, LocalGameState

from src.local_games import InstalledGame
from definitions import Blizzard


@pytest.mark.asyncio
async def test_local_games_states(plugin_mock):
    plugin_mock.local_client.get_running_games.return_value = set()
    plugin_mock.local_client.get_installed_games.return_value = {
        "test_game_id_1": InstalledGame(Blizzard['s1'], 's1', '1.0', '', '/path/', True),
    }

    expected_local_games = [
        LocalGame("test_game_id_1", LocalGameState.Installed)
    ]

    result = await plugin_mock.get_local_games()
    assert result == expected_local_games

