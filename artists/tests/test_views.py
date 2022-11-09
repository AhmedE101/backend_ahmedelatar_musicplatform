import pytest
from artists.models import Artist


@pytest.mark.django_db
def test_list_artists(Client):
    response = Client.get('http://127.0.0.1:8000/artists/api')
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_artists(Client):

    post_data = {
        'stage_name': 'eminem',
        'social_link': 'https://www.instagram.com/eminem/'}

    response = Client.post('http://127.0.0.1:8000/artists/api', post_data)
    assert response.data == {
        'stage_name': 'eminem',
        'social_link': 'https://www.instagram.com/eminem/'
    }


@pytest.mark.django_db
def test_create_artists_with_err(Client):

    post_data = {'stage_name': 'emine m',
                 'social_link': 'https://www.instagram.com/emi'}
    response = Client.post('http://127.0.0.1:8000/artists/api', post_data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_Artist_unique_name(client, user):
    data = {
        'stage_name': 'eminem',
        'social_link': 'https://www.instagram.com/eminem/'}

    response = client.post('http://localhost:8000/artists/', data)
    response = client.post('http://localhost:8000/artists/', data)
    assert response.status_code == 403
