import pytest
from definitions import Blizzard, BlizzardGame


def test_blizzard_getitem_no_item():
    with pytest.raises(KeyError):
        Blizzard['-1']


def test_blizzard_getitem_by_uid():
    for game in Blizzard.BATTLENET_GAMES + Blizzard.CLASSIC_GAMES:
        assert Blizzard[game.uid] == game


def test_blizzard_game_by_title_id_no_item():
    with pytest.raises(KeyError):
        Blizzard.game_by_title_id('-1', cn=False)


@pytest.mark.parametrize('cn, title_id, expected', [
    (True, '17459', Blizzard['d3cn']),
    (False, '17459', Blizzard['diablo3']),
    (True, '21297', Blizzard['s1']),
    (False, '21297', Blizzard['s1'])
])
def test_blizzard_game_by_title_id_cn(cn, title_id, expected):
    """d3cn should overwrite diablo3 for cn region"""
    assert Blizzard.game_by_title_id(title_id, cn) == expected


def test_try_for_free_games_no_d3cn():
    assert Blizzard['diablo3'] in Blizzard.try_for_free_games(cn=False)
    assert Blizzard['d3cn'] not in Blizzard.try_for_free_games(cn=False)
    # diablo3 not available for free in china
    assert Blizzard['d3cn'] not in Blizzard.try_for_free_games(cn=True)
