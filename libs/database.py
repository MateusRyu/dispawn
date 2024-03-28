from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
from os import getenv


def get_database(database = None):
    CONNECTION_STRING = getenv("MONGODB_TOKEN")
    client = MongoClient(uri, server_api=ServerApi('1'))

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
