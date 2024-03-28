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


