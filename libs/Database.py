from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri, server_api=ServerApi('1'))

    def ping(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return True
        except Exception as e:
            print(e)
            return False
