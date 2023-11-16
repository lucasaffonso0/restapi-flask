from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'port': 27017,
    'host': 'mongodb',
    'username': 'admin',
    'password': 'admin'
}

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help='This field cannot be blank.')
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help='This field cannot be blank.')
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help='This field cannot be blank.')
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help='This field cannot be blank.')
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help='This field cannot be blank.')

api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True, max_length=50)
    last_name = db.StringField(required=True, max_length=50)
    email = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)


class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())
        # return {'message': 'user 1'}


class User(Resource):
    def post(self):
        data = _user_parser.parse_args()
        UserModel(**data).save()

    def get(self, cpf):
        return {'message': 'CPF'}


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
