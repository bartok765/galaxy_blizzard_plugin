import pytest

from galaxy.api.types import LocalGame
from galaxy.api.consts import LocalGameState

from src.local_games import InstalledGame
from definitions import Blizzard


@pytest.mark.parametrize("installed, playable, expected_state", [
    (True, True, LocalGameState.Installed),
    (True, False, LocalGameState.Installed),
    (False, True, LocalGameState.Installed),
    (False, False, LocalGameState.None_),
])
@pytest.mark.asyncio
async def test_local_games_states(plugin_mock, installed, playable, expected_state):
    plugin_mock.local_client.get_running_games.return_value = set()
    plugin_mock.local_client.get_installed_games.return_value = {
        "test_game_id_1": InstalledGame(Blizzard['s1'], 's1', '1.0', '', '/path/', playable, installed),
    }

    expected_local_games = [
        LocalGame("test_game_id_1", expected_state)
    ]

    result = await plugin_mock.get_local_games()
    assert result == expected_local_games
