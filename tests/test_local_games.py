from unittest.mock import Mock, patch
from typing import NamedTuple

import pytest

from galaxy.api.types import LocalGame
from galaxy.api.consts import LocalGameState

from local_games import InstalledGame
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
        "s1": InstalledGame(Blizzard['s1'], 's1', '1.0', '', '/path/', playable, installed),
    }
    expected_local_games = [
        LocalGame("s1", expected_state)
    ]

    result = await plugin_mock.get_local_games()
    assert result == expected_local_games


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
def test_local_game_installation_state_notification(plugin_mock, prev, refr, new_state):

    def installed_game(playable: bool, installed: bool):
        with patch('local_games.pathfinder'):
            last_played = ''  # to not affect the logic for running game detection
            return InstalledGame(
                Mock(Blizzard), Mock(str), Mock(str), last_played, Mock(str),
                playable=playable, installed=installed
            )

    plugin_mock.update_local_game_status = Mock()
    game_id = 's1'
    previous_games = {game_id: installed_game(prev.playable, prev.installed)} if prev else {}
    refreshed_games = {game_id: installed_game(refr.playable, refr.installed)} if refr else {}
    
    plugin_mock._update_statuses(refreshed_games, previous_games)

    if new_state is None:
        plugin_mock.update_local_game_status.assert_not_called()
    else:
        local_game = LocalGame(game_id, new_state)
        plugin_mock.update_local_game_status.assert_called_once_with(local_game)


@pytest.mark.parametrize("prev_last_played, refr_last_played, new_state", [
    pytest.param('', '', None, id="game never played on this machine"),
    pytest.param('', '123123123', LocalGameState.Running | LocalGameState.Installed, id="game started for the first time on this machine"),
    pytest.param('11111111', '12222222', LocalGameState.Running | LocalGameState.Installed, id="game started"),
])
def test_local_game_running_state_notification(
    plugin_mock, prev_last_played, refr_last_played, new_state
):
    # patch side-effects
    plugin_mock._notify_about_game_stop = Mock()
    plugin_mock.create_task = Mock()

    plugin_mock.update_local_game_status = Mock()
    game_id = 's1'
    prev = Mock(InstalledGame, has_galaxy_installed_state=True, last_played=prev_last_played)
    refr = Mock(InstalledGame, has_galaxy_installed_state=True, last_played=refr_last_played)
    previous_games = {game_id: prev}
    refreshed_games = {game_id: refr}
    
    plugin_mock._update_statuses(refreshed_games, previous_games)

    if new_state is None:
        plugin_mock.update_local_game_status.assert_not_called()
    else:
        local_game = LocalGame(game_id, new_state)
        plugin_mock.update_local_game_status.assert_called_once_with(local_game)
