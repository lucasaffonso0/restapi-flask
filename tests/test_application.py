import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
                "first_name": "José",
                "last_name": "Lucas",
                "cpf": "887.001.790-78",
                "email": "teste@gmail.com",
                "birth_date": "2000-05-10"
            }

    @pytest.fixture
    def invalid_user(self):
        return {
                "first_name": "José",
                "last_name": "Lucas",
                "cpf": "887.001.790-71",
                "email": "teste@gmail.com",
                "birth_date": "2000-05-10"
            }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_users(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b'successfully' in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b'invalid' in response.data

    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get(f'/user/{valid_user["cpf"]}')
        assert response.status_code == 200
        assert response.json[0]['first_name'] == 'José'
        assert response.json[0]['last_name'] == 'Lucas'
        assert response.json[0]['cpf'] == '887.001.790-78'
        assert response.json[0]['email'] == 'teste@gmail.com'
        birth_date = response.json[0]['birth_date']['$date']
        assert birth_date == '2000-05-10T00:00:00Z'

        response = client.get(f'/user/{invalid_user["cpf"]}')
        assert response.status_code == 404
        assert b'User does not' in response.data

    def test_patch_users(self, client, valid_user):
        valid_user["first_name"] = "Joseé"
        response = client.patch('/user', json=valid_user)
        assert response.status_code == 200
        assert b'updated' in response.data

        valid_user["cpf"] = "878.197.570-86"
        response = client.patch('/user', json=valid_user)
        assert response.status_code == 404
        assert b'does not exist in database' in response.data
