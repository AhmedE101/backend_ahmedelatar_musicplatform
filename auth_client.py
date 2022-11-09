import pytest
from artists.models import Artist
from users.models import User
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient
from knox.models import AuthToken


@pytest.fixture()
def artists(db):
    artists = Artist.objects.create(
        stage_name='eminem',
        social_link='https://www.instagram.com/eminem/'
    )


@pytest.fixture()
def user(db):
    user = User.objects.create_user(email='email.com',
                                    username='AhmedElatar',
                                    password='chili')
    return user


@pytest.fixture()
def auth_client(user):
    client = APIClient()
    _, token = AuthToken.objects.create(user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client


@pytest.fixture
def client():
    return RequestsClient()


@pytest.fixture
def Client():
    return APIClient()
