from django.test import Client
from user.models import User, Pet
from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestCBViews:

    @pytest.mark.urls('purple.urls')
    def test_api_user_list_view_called(self, api_client):
        users = mixer.cycle(5).blend(User)
        response = api_client.get('/api/users/')
        res_data = response.data

        assert len(res_data) == 5

    @pytest.mark.urls('purple.urls')
    def test_api_user_detail_view_called(self, api_client):
        user = mixer.blend(User, email='test@test.com')
        response = api_client.get('/api/users/test@test.com/')
        res_data = response.data

        assert res_data['email'] == 'test@test.com'

    @pytest.mark.urls('purple.urls')
    def test_api_user_view_create(self, api_client):
        response = api_client.post(
            '/api/users/',
            {
                'email': 'test@test.com',
                'name': 'tester',
                'phone': '010-9999-1231'
            },
            format='json'
            )

        assert response.status_code == 201

    @pytest.mark.urls('purple.urls')
    def test_api_user_view_update(self, api_client):
        user = mixer.blend(
            User,
            email='test@test.com',
            name='tester',
            phone='010-9898-9999'
            )

        response = api_client.put(
            '/api/users/test@test.com/',
            {
                'email': 'test@test.com',
                'name': 'new_tester',
                'phone': '010-9898-9999'
            },
            format='json'
            )

        assert response.status_code == 200

    @pytest.mark.urls('purple.urls')
    def test_api_user_view_delete(self, api_client):
        user = mixer.blend(
            User,
            email='test@test.com',
            name='tester',
            phone='010-9898-9999'
            )

        response = api_client.delete('/api/users/test@test.com/')

        assert response.status_code == 204

    @pytest.mark.urls('purple.urls')
    def test_api_pet_list_view_called(self, api_client):
        pets = mixer.cycle(5).blend(Pet)
        response = api_client.get('/api/pets/')
        res_data = response.data

        assert len(res_data) == 5

    @pytest.mark.urls('purple.urls')
    def test_api_pet_detail_view_called(self, api_client):
        pet = mixer.blend(Pet, pk=1)
        response = api_client.get('/api/pets/1/')
        res_data = response.data

        assert res_data['id'] == 1

    @pytest.mark.urls('purple.urls')
    def test_api_pet_view_create(self, api_client):
        user = mixer.blend(User, email='test@test.com')

        response = api_client.post(
            '/api/pets/',
            {
                'owner': 'test@test.com',
                'name': 'mandoo'
            },
            format='json'
            )

        assert response.status_code == 201

    @pytest.mark.urls('purple.urls')
    def test_api_pet_view_update(self, api_client):
        user = mixer.blend(User, email='test@test.com')

        get_response = api_client.post(
            '/api/pets/',
            {
                'owner': 'test@test.com',
                'name': 'mandoo'
            },
            format='json'
            )
        
        pet_pk = get_response.json()['id']

        post_response = api_client.put(
            f'/api/pets/{pet_pk}/',
            {
                'owner': 'test@test.com',
                'name': 'king_mandoo'
            },
            format='json'
            )

        assert post_response.status_code == 200

    @pytest.mark.urls('purple.urls')
    def test_api_pet_view_delete(self, api_client):
        user = mixer.blend(User, email='test@test.com')

        get_response = api_client.post(
            '/api/pets/',
            {
                'owner': 'test@test.com',
                'name': 'mandoo'
            },
            format='json'
            )
        
        pet_pk = get_response.json()['id']

        del_response = api_client.delete(f'/api/pets/{pet_pk}/')

        assert del_response.status_code == 204

    @pytest.mark.urls('purple.urls')
    def test_user_list_view_called(self, client):
        users = mixer.cycle(5).blend(User)
        response = client.get('/users/')
        res_data = response.context_data

        assert res_data['user_list'].count() == 5

    @pytest.mark.urls('purple.urls')
    def test_user_detail_view_called(self, client):
        user = mixer.blend(User, email='test@test.com')
        response = client.get('/users/test@test.com/')
        res_data = response.context_data

        assert res_data['user'] == user

    @pytest.mark.urls('purple.urls')
    def test_pet_list_view_called(self, client):
        pets = mixer.cycle(5).blend(Pet, representative=False)
        response = client.get('/pets/')
        res_data = response.context_data

        assert res_data['pet_list'].count() == 5

    @pytest.mark.urls('purple.urls')
    def test_pet_detail_view_called(self, client):
        pet = mixer.blend(Pet, pk=1)
        response = client.get('/pets/1/')
        res_data = response.context_data

        assert res_data['pet'] == pet