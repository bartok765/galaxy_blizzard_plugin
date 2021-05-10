from unittest.mock import Mock, patch, call
from typing import NamedTuple, Optional

import pytest

from galaxy.api.types import LocalGame
from galaxy.api.consts import LocalGameState

from local_games import InstalledGame, get_directory_size
from definitions import Blizzard


@pytest.mark.parametrize("installed, playable, expected_state", [
    (True, True, LocalGameState.Installed),
    (True, False, LocalGameState.Installed),
    (False, True, LocalGameState.Installed),
])
@pytest.mark.asyncio
async def test_get_local_games_installed(plugin_mock, installed, playable, expected_state):
    expected_local_games = [
        LocalGame("s1", expected_state)
    ]

    plugin_mock.local_client.get_running_games.return_value = set()
    plugin_mock.local_client.get_installed_games.return_value = {
        "s1": InstalledGame(Blizzard['s1'], 's1', '1.0', '', '/path/', playable, installed),
    }

    assert await plugin_mock.get_local_games() == expected_local_games


@pytest.mark.asyncio
async def test_get_local_games_not_installed(plugin_mock):
    playable, installed = False, False
    expected_local_games = []

    plugin_mock.local_client.get_running_games.return_value = set()
    plugin_mock.local_client.get_installed_games.return_value = {
        "s1": InstalledGame(Blizzard['s1'], 's1', '1.0', '', '/path/', playable, installed),
    }
    
    assert await plugin_mock.get_local_games() == expected_local_games


class BlizzardGameState(NamedTuple):
    playable: bool
    installed: bool


@pytest.mark.parametrize("prev, refr, new_state", [
    pytest.param(
        BlizzardGameState(True, True),
        BlizzardGameState(True, True),
        None,
        id="no change; game playable"
    ),
    pytest.param(
        None,
        BlizzardGameState(False, False), 
        None,
        id="game installation began or first iteration after plugin start"
    ),
    pytest.param(
        None,
        BlizzardGameState(True, False), 
        LocalGameState.Installed,
        id="first iteration after plugin start: game is playable"
    ),
    pytest.param(
        None,
        BlizzardGameState(False, True), 
        LocalGameState.Installed,
        id="first iteration after plugin start: game not playable but installed (eg. update pending)"
    ),
    pytest.param(
        BlizzardGameState(False, False), 
        BlizzardGameState(True, True), 
        LocalGameState.Installed,
        id="game installation finished"
    ),
    pytest.param(
        BlizzardGameState(False, False), 
        BlizzardGameState(True, False), 
        LocalGameState.Installed,
        id="game became playable during installation"
    ),
    pytest.param(
        BlizzardGameState(True, False),
        BlizzardGameState(True, True), 
        None,
        id="playable game fully installed"
    ),
    pytest.param(
        BlizzardGameState(True, True),
        BlizzardGameState(False, True), 
        None,
        id="game update appeared"
    ),
    pytest.param(
        BlizzardGameState(False, True),
        BlizzardGameState(True, True), 
        None,
        id="game update finished"
    ),
    pytest.param(
        BlizzardGameState(True, True), 
        None, 
        LocalGameState.None_,
        id="game uninstalled"
    ),
])
def test_local_game_installation_state_notification(
    plugin_mock,
    prev: Optional[BlizzardGameState],
    refr: Optional[BlizzardGameState],
    new_state: Optional[LocalGameState]
):

    def installed_game(playable: bool, installed: bool):
        with patch('local_games.pathfinder'):
            last_played = ''  # to not affect the logic for running game detection
            return InstalledGame(
                Mock(Blizzard), Mock(str), Mock(str), last_played, Mock(str),
                playable=playable, installed=installed
            )

    plugin_mock.update_local_game_status = Mock()
    GAME_ID = 's1'
    previous_games = {GAME_ID: installed_game(prev.playable, prev.installed)} if prev else {}
    refreshed_games = {GAME_ID: installed_game(refr.playable, refr.installed)} if refr else {}
    
    plugin_mock._update_statuses(refreshed_games, previous_games)

    if new_state is None:
        plugin_mock.update_local_game_status.assert_not_called()
    else:
        local_game = LocalGame(GAME_ID, new_state)
        plugin_mock.update_local_game_status.assert_called_once_with(local_game)


@pytest.mark.parametrize("prev_last_played, refr_last_played, new_state", [
    pytest.param('', '', None, id="game never played on this machine"),
    pytest.param('', '123123123', LocalGameState.Running | LocalGameState.Installed, id="game started for the first time on this machine"),
    pytest.param('11111111', '12222222', LocalGameState.Running | LocalGameState.Installed, id="game started"),
])
def test_local_game_running_state_notification(
    plugin_mock,
    prev_last_played: str,
    refr_last_played: str,
    new_state: Optional[LocalGameState]
):
    # patch side-effects
    plugin_mock._notify_about_game_stop = Mock()
    plugin_mock.create_task = Mock()

    plugin_mock.update_local_game_status = Mock()
    GAME_ID = 's1'
    previous_games = {GAME_ID: Mock(InstalledGame, has_galaxy_installed_state=True, last_played=prev_last_played)}
    refreshed_games = {GAME_ID: Mock(InstalledGame, has_galaxy_installed_state=True, last_played=refr_last_played)}
    
    plugin_mock._update_statuses(refreshed_games, previous_games)

    if new_state is None:
        plugin_mock.update_local_game_status.assert_not_called()
    else:
        local_game = LocalGame(GAME_ID, new_state)
        plugin_mock.update_local_game_status.assert_called_once_with(local_game)


def test_local_game_notification_multiple_games(plugin_mock):
    # patch side-effects
    plugin_mock._notify_about_game_stop = Mock()
    plugin_mock.create_task = Mock()

    plugin_mock.update_local_game_status = Mock()
    previous_games = {
        'hs_beta': Mock(InstalledGame, has_galaxy_installed_state=True, last_played=''),
        's2': Mock(InstalledGame, has_galaxy_installed_state=True, last_played=''),
    }
    refreshed_games = {
        's1': Mock(InstalledGame, has_galaxy_installed_state=True, last_played=''),
        's2': Mock(InstalledGame, has_galaxy_installed_state=True, last_played='12313111'),
    }

    plugin_mock._update_statuses(refreshed_games, previous_games)

    plugin_mock.update_local_game_status.assert_has_calls([
            call(LocalGame('hs_beta', LocalGameState.None_)),
            call(LocalGame('s1', LocalGameState.Installed)),
            call(LocalGame('s2', LocalGameState.Installed | LocalGameState.Running)),
        ],
        any_order=True
    )

    
def test_get_directory_size(tmp_path):
    def create_file(path: str, content: bytes) -> int:
        path.parent.mkdir(exist_ok=True, parents=True)
        return path.write_bytes(content)

    expected_size = sum(
        create_file(p, c) for p, c in [
            (tmp_path / 'readme.txt', b'Readme content'),
            (tmp_path / 'assets' / 'de.pack', b'dummy binary file content'),
            (tmp_path / 'bin' / 'game.exe', b'0\05sdcdsdj9asfsdf\nfaf22e' * 1000000)
        ]
    )
    assert get_directory_size(tmp_path) == expected_size
