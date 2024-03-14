from libs.chess_crawler import get_player

def test_get_player_return_structure():
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

