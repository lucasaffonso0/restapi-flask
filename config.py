import os
import mongomock


class DevConfig():
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB'),
        'host': os.getenv('MONGO_HOST'),
        'username': os.getenv('MONGO_USER'),
        'password': os.getenv('MONGO_PASSWORD')
    }


class MockConfig:
    MONGODB_SETTINGS = {
        'db': 'users',
        'host': 'mongodb://localhost',
        'mongo_client_class': mongomock.MongoClient
    }


class ProdConfig():
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB'),
        'host': os.getenv('MONGO_HOST'),
        'username': os.getenv('MONGO_USER'),
        'password': os.getenv('MONGO_PASSWORD')
    }
