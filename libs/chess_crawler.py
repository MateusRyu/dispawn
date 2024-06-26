from urllib.request import urlopen
from urllib.error import HTTPError
import json

TITLES = ["GM", "WGM", "IM", "WIM", "FM", "WFM", "NM", "WNM", "CM", "WCM"]

def get_player(username):
    url = f"https://api.chess.com/pub/player/{username}"

    try:
        response = urlopen(url)
        data = json.load(response)

        country_response = urlopen(data["country"])
        data["country"] = json.load(country_response)
    except HTTPError as error:
        if error.code == 404:
            print(f"Error 404: username '{username}' not found.")
        else:
            prin(f"Error {error.code}: search failed.")
        return False
    except Exception as error:
        print(f"Error: {error}.")
        return False

    return data

def get_titled_player_usernames_by_title(title_abbreviation):
    if title_abbreviation not in TITLES:
        return False
    url = f"https://api.chess.com/pub/titled/{title_abbreviation}"
    response = urlopen(url)
    data = json.load(response)
    return data["players"]

def get_player_stats(username):
    url = f"https://api.chess.com/pub/player/{username}/stats"

    try:
        response = urlopen(url)
        data = json.load(response)
    except HTTPError as error:
        if error.code == 404:
            print(f"Error 404: username '{username}' not found.")
        else:
            prin(f"Error {error.code}: search failed.")
        return False
    except Exception as error:
        print(f"Error: {error}.")
        return False

    return data

def get_player_archives(username):
    url = f"https://api.chess.com/pub/player/{username}/games/archives"
    
    try:
        response = urlopen(url)
        data = json.load(response)
    except HTTPError as error:
        if error.code == 404:
            print(f"Error 404: username '{username}' not found.")
        else:
            prin(f"Error {error.code}: search failed.")
        return False
    except Exception as error:
        print(f"Error: {error}.")
        return False

    return data

