import pytest

from galaxy.api.types import LocalGame
from galaxy.api.consts import LocalGameState

from src.local_games import InstalledGame
from definitions import Blizzard


@pytest.mark.parametrize("total_to_download, playable, state", [
    (0, True, LocalGameState.Installed),
    (1234, True, LocalGameState.Installed),
    (1234, False, LocalGameState.Installed),
    (0, False, LocalGameState.None_),
])
@pytest.mark.asyncio
async def test_local_games_states(plugin_mock, total_to_download, playable, state):
    plugin_mock.local_client.get_running_games.return_value = set()
    plugin_mock.local_client.get_installed_games.return_value = {
        "test_game_id_1": InstalledGame(Blizzard['s1'], 's1', '1.0', '', '/path/', playable, total_to_download),
    }

    expected_local_games = [
        LocalGame("test_game_id_1", state)
    ]

    result = await plugin_mock.get_local_games()
    assert result == expected_local_games
