import os


class DevConfig():
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB'),
        'host': os.getenv('MONGO_HOST'),
        'username': os.getenv('MONGO_USER'),
        'password': os.getenv('MONGO_PASSWORD')
    }


class ProdConfig():
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB'),
        'host': os.getenv('MONGO_HOST'),
        'username': os.getenv('MONGO_USER'),
        'password': os.getenv('MONGO_PASSWORD')
    }
