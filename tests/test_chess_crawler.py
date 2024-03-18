from pytest import mark
from urllib.request import urlopen
from urllib.error import HTTPError
from libs.chess_crawler import *

@mark.api
def test_get_player_return_type():
    input = "kanna_yukari"
    result = get_player(input)
    
    assert isinstance(result, dict), "Result must be a dictionary"

    expect_keys = [
        'avatar', 'player_id', '@id', 'url', 'name', 'username','followers', 
        'country', 'last_online', 'joined', 'status', 'is_streamer', 'verified', 'league'
    ]

    expected_types = {
        'avatar': str,
        'player_id': int,
        '@id': str,
        'url': str,
        'name': str,
        'username': str,
        'followers': int,
        'country': str,
        'last_online': int,
        'joined': int,
        'status': str,
        'is_streamer': bool,
        'verified': bool,
        'league': str
    }

    assert all(key in result for key in expect_keys), "Some keys are missing"

    for key, expected_type in expected_types.items():
        assert isinstance(result[key], expected_type), f"The value for '{key}' must be type of {expected_type.__name__}"

@mark.api
def test_get_player_with_a_username_that_does_not_exist():
    input = 2 * "a"
    result = get_player(input)
    assert result == False 

@mark.api
def test_get_player_with_a_empty_username():
    input = ""
    result = get_player(input)
    assert result == False

@mark.xfail(not check_internet_conection(), reason="This test need  a internet connection.")

@mark.api
def test_get_player_return_structure():
    for title in TITLES:
        players = get_titled_player_usernames_by_title(title)
        assert isinstance(players, list)

        for player in players:
            assert isinstance(player, str)
