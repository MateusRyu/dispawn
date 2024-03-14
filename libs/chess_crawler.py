from urllib.request import urlopen
import json

def get_player(username):
    url = f"https://api.chess.com/pub/player/{username}"
    response = urlopen(url)
    data = json.load(response)
    return data

