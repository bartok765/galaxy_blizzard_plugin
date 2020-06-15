import pytest
from parsers import DatabaseParser, ProductDbInfo, ConfigParser, ConfigGameInfo


def test_config_parser_decode_installed():
    parser = ConfigParser(None)
    games = parser.decode({ "s1": {
            "ServerUid": "s1",
            "Resumable": "false"
        }
    })
    assert games[0].uid == "s1"
    assert games[0].uninstall_tag == "s1"


def test_config_parser_decode_last_played():
    parser = ConfigParser(None)
    games = parser.decode({ "s2": { "LastPlayed": "1552039613" } })
    assert games[0].uid == "s2"
    assert games[0].uninstall_tag == None
    assert games[0].last_played == '1552039613'


def test_config_parser(config_data):
    parser = ConfigParser(config_data)
    assert parser.locale_language == 'plPL'
    assert parser.region == 'EU'
    assert ConfigGameInfo('diablo3', 'diablo3_plpl', None) in parser.games
    assert ConfigGameInfo('heroes', None, '1441712029') in parser.games
    assert ConfigGameInfo('wow', 'wow_enus', None) in parser.games


def test_db_parser(load_database):
    prs = DatabaseParser(load_database)
    assert prs.products.get('agent') == ProductDbInfo('agent', 'agent', 'C:/ProgramData/Battle.net/Agent', '2.16.3.6610', True)
    assert prs.products.get('bna') == ProductDbInfo('battle.net', 'bna', 'C:/Program Files (x86)/Battle.net', '1.12.8.10949', True)
    assert prs.products.get('s1') == ProductDbInfo('s1', 's1', 'C:/Program Files (x86)/StarCraft', '1.22.3.5354', True)
    assert prs.products.get('d3') == ProductDbInfo('diablo3_plpl', 'd3', 'C:/Program Files (x86)/Diablo III', '2.6.4.55430', True)


def test_db_parser2(another_database):
    parser = DatabaseParser(another_database)
    assert parser.products.get('s1') == ProductDbInfo('s1', 's1', 'D:/bnet/StarCraft', '1.22.3.5354', True)


def test_db_parser3_games_under_installation(db_under_installation):
    prs = DatabaseParser(db_under_installation)
    assert prs.products.get('s1') == ProductDbInfo('s1', 's1', 'C:/Program Files (x86)/StarCraft', '', False)
    assert prs.products.get('hero') == ProductDbInfo('heroes', 'hero', 'C:/Program Files (x86)/Heroes of the Storm', '2.43.3.72649', True)
