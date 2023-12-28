import os
import mongomock


class DevConfig:
    MONGODB_SETTINGS = {
        "db": os.getenv("MONGO_DB"),
        "host": os.getenv("MONGO_HOST"),
        "username": os.getenv("MONGO_USER"),
        "password": os.getenv("MONGO_PASSWORD"),
    }


class MockConfig:
    MONGODB_SETTINGS = {
        "db": "users",
        "host": "mongodb://localhost",
        "mongo_client_class": mongomock.MongoClient,
    }


class ProdConfig:
    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_DB = os.getenv("MONGODB_DB")
    REPLICASET = "replicaSet=atlas-qkejxn-shard-0"
    AUTH = "authSource=admin&retryWrites=true&w=majority"
    MONGODB_SETTINGS = {
        "host": "mongodb://%s:%s@%s:27017/%s?ssl=true&%s&%s"
        % (MONGODB_USER, MONGODB_PASSWORD, MONGODB_HOST, MONGODB_DB, REPLICASET, AUTH)
    }
