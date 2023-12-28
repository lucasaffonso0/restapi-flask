from .db import db


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True, max_length=50)
    last_name = db.StringField(required=True, max_length=50)
    email = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)


class HealthCheckModel(db.Document):
    status = db.StringField(required=True)
