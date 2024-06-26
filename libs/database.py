from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
from os import getenv


def get_database(database = None):
    CONNECTION_STRING = getenv("MONGODB_TOKEN")
    client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))

    return client[database]


def ping():
    client = get_database()
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(e)
        return False


def insert_club(guild_id, club_link, name):
    db = get_database("guild")
    club_collection = db["clubs"]
    query = {"guild_id": guild_id, "club_link": club_link, "club_name": name}
    request = club_collection.insert_one(query)
    return request.inserted_id

def get_club(guild_id):
    db = get_database("guild")
    club_collection = db["clubs"]
    query = {"guild_id": guild_id}
    result = club_collection.find(query)

    for item in result:
        club = item

    if "club" in locals():
        return club
    return False


def update_club(guild_id, new_values):
    db = get_database("guild")
    club_collection = db["clubs"]
    filter = {"guild_id": guild_id}
    values = {"$set": new_values}
    result = club_collection.update_one(filter, values)
    return result

def delete_club(guild_id):
    db = get_database("guild")
    club_collection = db["clubs"]
    result = club_collection.delete_one({"guild_id": guild_id})
    return result

def insert_player(guild_id, user_id, site, username, invite_link):
    db = get_database("player")
    players_collection = db[site]
    query = {"guild_id": guild_id, "user_id": user_id, "username": username, "invite_link": invite_link}
    request = players_collection.insert_one(query)
    return request.inserted_id

def get_player(guild_id, user_id, site):
    db = get_database("player")
    player_collection = db[site]
    query = {"guild_id": guild_id, "user_id": user_id}
    result = player_collection.find(query)

    for item in result:
        player = item

    if "player" in locals():
        return player 
    return False

def get_all_players(guild_id, site):
    db = get_database("player")
    player_collection = db[site]
    query = {"guild_id": guild_id}
    result = player_collection.find(query)
    players = []
        
    for item in result:
        player.append(item)
    return players


def update_player(guild_id, user_id, site, new_values):
    db = get_database("player")
    player_collection = db[site]
    filter = {"guild_id": guild_id, "user_id": user_id}
    values = {"$set": new_values}
    result = player_collection.update_one(filter, values)
    return result


def delete_player(guild_id, user_id, site):
    db = get_database("player")
    player_collection = db[site]
    result = player_collection.delete_one({"guild_id": guild_id, "user_id": user_id})
    return result
