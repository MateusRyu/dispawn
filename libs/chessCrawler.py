from urllib.request import urlopen
import json

def getPlayer(username):
    url = f"https://api.chess.com/pub/player/{username}"
    response = urlopen(url)
    data = json.load(response)
    return data

