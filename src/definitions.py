import dataclasses as dc
import json
import requests
from typing import Optional, Dict, List


class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dc.is_dataclass(o):
            return dc.asdict(o)
        return super().default(o)


@dc.dataclass
class WebsiteAuthData(object):
    cookie_jar: requests.cookies.RequestsCookieJar
    access_token: str
    region: str


@dc.dataclass
class BlizzardGame:
    uid: str
    name: str
    family: str


@dc.dataclass
class BattlenetGame(BlizzardGame):
    free_to_play: bool


@dc.dataclass
class ClassicGame(BlizzardGame):
    registry_path: Optional[str] = None
    registry_installation_key: Optional[str] = None
    exe: Optional[str] = None
    bundle_id: Optional[str] = None


@dc.dataclass
class ConfigGameInfo(object):
    uid: str
    uninstall_tag: Optional[str]
    last_played: Optional[str]


@dc.dataclass
class ProductDbInfo(object):
    uninstall_tag: str
    ngdp: str = ''
    install_path: str = ''
    version: str = ''
    playable: bool = False


class Singleton(type):
    _instances = {}  # type: ignore

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class _Blizzard(object, metaclass=Singleton):
    BACKEND_ID_UID = {
        '21297': 's1',
        '21298': 's2',
        '5730135': 'wow',
        '5272175': 'prometheus',
        '?': 'w3',  # TODO ask for help in Readme
        '1146311730': 'destiny2',
        '1465140039': 'hs_beta',
        '1214607983': 'heroes',
        '17459': 'diablo3',
        '1447645266': 'viper',
        '1329875278': 'odin'
    }
    BACKEND_ID_UID_CN = {
        **BACKEND_ID_UID,
        '17459': 'd3cn'
    }

    BATTLENET_GAMES = {
        BattlenetGame('s1', 'StarCraft', 'S1', True),
        BattlenetGame('s2', 'StarCraft II', 'S2', True),
        BattlenetGame('wow', 'World of Warcraft', 'WoW', True),
        BattlenetGame('wow_classic', 'World of Warcraft Classic', 'WoW_wow_classic', False),
        BattlenetGame('prometheus', 'Overwatch', 'Pro', False),
        BattlenetGame('w3', 'Warcraft III', 'W3', False),
        BattlenetGame('destiny2', 'Destiny 2', 'DST2', False),
        BattlenetGame('hs_beta', 'Hearthstone', 'WTCG', True),
        BattlenetGame('heroes', 'Heroes of the Storm', 'Hero', True),
        BattlenetGame('d3cn', '暗黑破壞神III', 'D3CN', False),
        BattlenetGame('diablo3', 'Diablo III', 'D3', True),
        BattlenetGame('viper', 'Call of Duty: Black Ops 4', 'VIPR', False),
        BattlenetGame('odin', 'Call of Duty: Modern Warfare', 'ODIN', False),
    }

    CLASSIC_GAMES = [
        ClassicGame('d2', 'Diablo® II', 'Diablo II', 'Diablo II', 'DisplayIcon', "Game.exe", "com.blizzard.diabloii"),
        ClassicGame('d2LOD', 'Diablo® II: Lord of Destruction®', 'Diablo II'),  # TODO exe and bundleid
        ClassicGame('w3ROC', 'Warcraft® III: Reign of Chaos',  'Warcraft III', 'Warcraft III', 'InstallLocation', 'Warcraft III.exe', 'com.blizzard.WarcraftIII'),
        ClassicGame('w3tft', 'Warcraft® III: The Frozen Throne®',  'Warcraft III', 'Warcraft III', 'InstallLocation', 'Warcraft III.exe', 'com.blizzard.WarcraftIII'),
        ClassicGame('sca', 'StarCraft® Anthology', 'Starcraft', 'StarCraft')  # TODO exe and bundleid
    ]

    def __init__(self):
        self._games = {game.uid: game for game in self.BATTLENET_GAMES + self.CLASSIC_GAMES}

    def __getitem__(self, key: str):
        try:
            return self._games[key]
        except KeyError as e:  # check for family
            for g in self._games.values():
                if g.family == key:
                    return g
        raise e


Blizzard = _Blizzard()
