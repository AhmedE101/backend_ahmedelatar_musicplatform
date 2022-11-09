

def test_GET_User(user, auth_client):
    response = auth_client.get("http://127.0.0.1:8000/user/api_detail/1")

    assert response.data == {"email": "email.com",
                             'id': 1,
                             'username': 'AhmedElatar',
                             'bio': ''
                             }


def test_get_wrong_id(user, auth_client):
    response = auth_client.get('http://127.0.0.1:8000/user/api_detail/1000')
    assert response.status_code == 404


def test_update_put(auth_client, user):

    update_data = {
        "bio": "new addition",
        "username": "ahmedElatar",
        "email": "ahmedmido@gmail.com",
        "password": "chili251"
    }

    response = auth_client.put(f'/user/api_detail/{user.id}', update_data)

    assert response.data == {"bio": "new addition",
                             "email": "ahmedmido@gmail.com",
                             'id': 1,
                             'username': 'ahmedElatar'}


def test_update_put_err(auth_client, user):

    update_data = {
        "bio": "new addition",
        "email": "ahmedmido@gmail.com",
        "password": "chili252"
    }

    response = auth_client.put(f'/user/api_detail/{user.id}', update_data)
    assert response.status_code == 400


def test_update_patch(auth_client, user):

    update_data = {
        "bio": "new addition",
        "username": "ahmedElatar"
    }

    response = auth_client.put(f'/user/api_detail/{user.id}', update_data)

    assert response.data == {'bio': 'new addition',
                             'email': 'email.com',
                             'id': 1,
                             'username': 'ahmedElatar'}
