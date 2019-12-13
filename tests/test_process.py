import pytest
from psutil import Process
from pathlib import PurePath


class MockProc():
    def __init__(self, path):
        self.path = path

    def username(self):
        return ""

    def exe(self):
        return self.path

    def name(self):
        return PurePath(self.path).name


@pytest.fixture()
def processes():
    return [
        "C:\\System\\svchost.exe",
        "C:\\Program Files (x86)\\StarCraft\\StarCraft.exe",
        "C:\\Program Files (x86)\\DiabloIII\\DiabloIII64.exe",
        "C:\\Users\\kazik\\AppData\\Local\\Programs\\Python\\Python37-32",
    ]


@pytest.fixture()
def s1_execs():
    return [
        "C:\\Program Files (x86)\\StarCraft\\StarCraft.exe",
        "C:\\Program Files (x86)\\StarCraft\\StarEdit.exe",
        "C:\\Program Files (x86)\\StarCraft\\BlizzardError.exe"
    ]


@pytest.fixture()
def mock_process_env(mocker):
    def function(procs):
        mocker.patch('psutil.process_iter', return_value=[n for n in range(len(procs))])
        mocker.patch('psutil.Process', autospec=True, side_effect=procs)
        mocker.patch.object(Process, 'username', 'mockuser')
    return function

