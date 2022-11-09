import pytest


@pytest.mark.django_db
def test_unAuthenticated(client):
    response = client.post('http://127.0.0.1:8000/authentication/api_register', json={
        "username": "AhmedElatar",
        "email": "ahmedelatar@gmail.com",
        "password1": "57xW!!G6&cUP",
        "password2": "57xW!!G6&cUP"
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_unAuthenticated_not_match_password(client):

    response = client.post('http://127.0.0.1:8000/authentication/api_register', json={
        "username": "AhmedElatar",
        "email": "ahmedelatar@gmail.com",
        "password1": "57xW!!G6&cUP",
        "password2": "57xW!!G6&cUP567"
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_unAuthenticated_forget_username(client):

    response = client.post('http://127.0.0.1:8000/authentication/api_register', json={
        "email": "ahmedelatar@gmail.com",
        "password1": "57xW!!G6&cUP",
        "password2": "57xW!!G6&cUP567"
    })
    assert response.status_code == 400


@pytest.mark.django_db
def test_login(client, user):

    response = client.post('http://127.0.0.1:8000/authentication/api_login', json={
        "username": "AhmedElatar",
        "password": "chili"
    })

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_not_exist(client):

    response = client.post('http://127.0.0.1:8000/authentication/api_login', json={
        "username": "AhmedElatar",
        "password": "chili1234"
    })

    assert response.status_code == 400


@pytest.mark.django_db
def test_logout(client, auth_client):

    # login first.
    client.post('http://127.0.0.1:8000/authentication/api_login', json={
        "username": "AhmedElatar",
        "password": "chili"
    })
    response = auth_client.post(
        'http://127.0.0.1:8000/authentication/api_logout')

    assert response.status_code == 200
