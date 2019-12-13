import pytest
from unittest import mock
from pathlib import Path

from src.pathfinder import PathFinder
from src.consts import Platform


@pytest.fixture()
def s1_dir_exe():
    return [
        ('StarCraft', ('editor',), ('Starcraft.exe',)),
        ('StarCraft\\editor', (), ('logs.logs', 'editor.exe')),
    ]


@pytest.fixture()
def s1_dir_no_exe():
    return [
        ('StarCraft', ('editor',), ('Starcraft',)),
        ('StarCraft\\editor', (), ('logs.logs', 'editor')),
    ]

@pytest.fixture()
def s1_dir_exe_mac():
    return [
        ('StarCraft', ('editor',), ('Starcraft',)),
        ('StarCraft/editor', (), ('logs.logs', 'editor')),
    ]


@mock.patch('os.walk')
@mock.patch.object(Path, 'exists', (lambda _: True))
def test_find_exec_win_empty(mock_walk, s1_dir_no_exe):
    mock_walk.return_value = s1_dir_no_exe
    execs = PathFinder(Platform.WINDOWS).find_executables('some_mock_path')
    assert execs == []


#~ @mock.patch('os.walk')
#~ @mock.patch.object(Path, 'exists', (lambda _: True))
#~ def test_find_exec_win(mock_walk, s1_dir_exe):
    #~ mock_walk.return_value = s1_dir_exe
    #~ execs = PathFinder(Platform.WINDOWS).find_executables('some_mock_path')
    #~ assert execs == ['StarCraft\\Starcraft.exe', 'StarCraft\\editor\\editor.exe']


@mock.patch('os.walk')
@mock.patch('os.path.join', (lambda x, y: '/'.join([x, y])))
@mock.patch.object(Path, 'exists', (lambda _: True))
def test_find_exec_mac(mock_walk, s1_dir_exe_mac):

    def define_execs(execs):
        def mock_access(path, _):
            return path in execs
        return mock_access

    expected = ['StarCraft/Starcraft', 'StarCraft/editor/editor']
    with mock.patch('os.access', define_execs(expected)):
        mock_walk.return_value = s1_dir_exe_mac
        execs = PathFinder(Platform.MACOS).find_executables('some_mock_path')
        assert execs == expected


