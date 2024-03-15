from urllib.request import urlopen
from urllib.error import HTTPError
import json

def get_player(username):
    url = f"https://api.chess.com/pub/player/{username}"

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
    response = urlopen(url)
    data = json.load(response)
    return data

