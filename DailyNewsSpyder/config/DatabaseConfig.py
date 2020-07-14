from pymongo import MongoClient

class DatabaseConfig():
    def __init__(self):
        self.db = MongoClient(
            "url_mongo"
        )['daily-news']

    def getCollection(self,collectionName):
        return self.db[collectionName]

    def resetCollection(self,collectionName):
        self.db[collectionName].drop()


