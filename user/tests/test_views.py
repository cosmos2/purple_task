import json

from django.test import Client
from mixer.backend.django import mixer
import pytest

from user.models import User, Pet


@pytest.mark.django_db
@pytest.mark.urls('purple.urls')
class TestUserViewSet:

    def test_get_list(self, api_client):
        users = mixer.cycle(5).blend(User)
        response = api_client.get('/api/users/')
        res_data = response.data

        assert len(res_data) == 5

    def test_get_detail(self, api_client):
        user = mixer.blend(User, email='pengsoo@cute.com')
        response = api_client.get('/api/users/pengsoo@cute.com/')
        res_data = response.data

        assert res_data['email'] == 'pengsoo@cute.com'

    def test_create(self, api_client):
        response = api_client.post(
            '/api/users/',
            {
                'email': 'pengsoo@cute.com',
                'name': 'tester',
                'phone': '010-9999-1231',
                'role': 'SU'
            },
            format='json'
            )

        assert response.status_code == 201

    def test_update(self, api_client):
        user = mixer.blend(
            User,
            email='pengsoo@cute.com',
            name='pengsoo',
            phone='010-9898-9999'
            )

        response = api_client.put(
            '/api/users/pengsoo@cute.com/',
            {
                'email': 'pengsoo@cute.com',
                'name': 'penguin',
                'phone': '010-9898-9999'
            },
            format='json'
            )

        assert response.status_code == 200

    def test_delete(self, api_client):
        user = mixer.blend(
            User,
            email='pengsoo@cute.com',
            name='tester',
            phone='010-9898-9999'
            )

        response = api_client.delete('/api/users/pengsoo@cute.com/')

        assert response.status_code == 204

@pytest.mark.django_db
@pytest.mark.urls('purple.urls')
class TestPetViewSet:

    def test_get_list(self, api_client):
        pets = mixer.cycle(5).blend(Pet)
        response = api_client.get('/api/pets/')
        res_data = response.data

        assert len(res_data) == 5

    def test_get_detail(self, api_client):
        pet = mixer.blend(Pet, pk=1, name='pengsoo')
        response = api_client.get('/api/pets/1/')
        res_data = response.data

        assert res_data['name'] == 'pengsoo'

    def test_create(self, api_client):
        user = mixer.blend(User, email='pengsoo@cute.com')

        response = api_client.post(
            '/api/pets/',
            {
                'owner': 'pengsoo@cute.com',
                'name': 'mandoo'
            },
            format='json'
            )

        assert response.status_code == 201

    def test_update(self, api_client):
        user = mixer.blend(
            User,
            email='pengsoo@cute.com',
            )
        pet = mixer.blend(
            Pet,
            owner=user,
            id=153,
            representative=True
        )

        post_response = api_client.put(
            '/api/pets/153/',
            {
                'owner': 'pengsoo@cute.com',
                'name': 'king_mandoo',
                'representative': False
            },
            format='json'
            )

        assert post_response.status_code == 200

    def test_delete(self, api_client):
        user = mixer.blend(User, email='pengsoo@cute.com')
        pet = mixer.blend(Pet, id=153, owner=user)

        del_response = api_client.delete(f'/api/pets/153/')

        assert del_response.status_code == 204

    def test_filter_owner(self, api_client):
        user = mixer.blend(User, email='pengsoo@cute.com')
        pets = mixer.cycle(10).blend(Pet, owner=user)

        response = api_client.get('/api/pets/?owner=pengsoo@cute.com')
        res_data = response.data

        assert len(res_data) == 10

    def test_filter_owner_with_rep(self, api_client):
        user = mixer.blend(User, email='pengsoo@cute.com')
        pets = mixer.cycle(10).blend(Pet, owner=user)
        rep_pet = mixer.blend(
            Pet,
            owner=user,
            representative=True
            )
        
        response = api_client.get(
            '/api/pets/?owner=pengsoo@cute.com&rep=true'
        )
        res_data = response.data

        assert len(res_data) == 1


@pytest.mark.django_db
@pytest.mark.urls('purple.urls')
class TestUserList:

    def test_get(self, client):
        users = mixer.cycle(5).blend(User)
        response = client.get('/users/')
        res_data = response.context_data

        assert res_data['user_list'].count() == 5

    def test_post(self, client):
        data = json.dumps({
            'email': 'pengsoo@cute.com',
            'name': 'tester',
            'phone': '010-9999-1231'
        })
        response = client.post(
            '/users/',
            data=data,
            content_type='application/json'
            )
        get_response = client.get('/users/pengsoo@cute.com/')

        assert response.status_code == 302  # redirect
        assert get_response.status_code == 200  # 생성확인


@pytest.mark.django_db
@pytest.mark.urls('purple.urls')
class TestUserDetail:

    def test_get(self, client):
        user = mixer.blend(User, email='pengsoo@cute.com')
        response = client.get('/users/pengsoo@cute.com/')
        res_data = response.context_data

        assert res_data['user'] == user

    def test_put(self, client):
        user = mixer.blend(User, email='pengsoo@cute.com')
        data = json.dumps({
            'email': 'pengsoo@cute.com',
            'name': 'pengsoo',
            'phone': '010-5678-9876',
            'role': 'SU'
        })

        response = client.put(
            '/users/pengsoo@cute.com/',
            data=data,
            content_type='application/json'
        )
        res_data = response.content.decode('ascii')

        assert res_data.find('010-5678-9876') != -1

    def test_delete(self, client):
        user = mixer.blend(User, email='mercury@space.com')

        response = client.delete('/users/mercury@space.com/', "{}")
        check_res = client.get('/users/mercury@space.com/')

        assert check_res.status_code == 404


@pytest.mark.django_db
@pytest.mark.urls('purple.urls')
class TestPetList:

    def test_get(self, client):
        pets = mixer.cycle(5).blend(Pet, representative=False)
        response = client.get('/pets/')
        res_data = response.context_data

        assert res_data['pet_list'].count() == 5

    def test_post(self, client):
        user = mixer.blend(User, email='pengsoo@cute.com')
        data = json.dumps({
            'owner': 'pengsoo@cute.com',
            'name': 'dragon',
            'illness': {
                'sick': 'stomachache'
            },
            'representative': True
        })
        response = client.post(
            '/pets/',
            data=data,
            content_type='application/json'
            )
        get_response = client.get('/users/pengsoo@cute.com/')

        assert response.status_code == 302  # redirect
        assert get_response.status_code == 200  # 생성확인

@pytest.mark.django_db
@pytest.mark.urls('purple.urls')
class TestPetDetail:

    def test_get(self, client):
        pet = mixer.blend(Pet, pk=1)
        response = client.get('/pets/1/')
        res_data = response.context_data

        assert res_data['pet'] == pet

    def test_put(self, client):
        user = mixer.blend(User, email='pengsoo@cute.com')
        pet = mixer.blend(Pet, id=153, owner=user)
        data = json.dumps({
            'owner': 'pengsoo@cute.com',
            'name': 'dragon',
            'illness': {
                'sick': 'stomachache'
            },
            'representative': True
        })

        response = client.put(
            '/pets/153/',
            data=data,
            content_type='application/json'
        )
        res_data = response.content.decode('ascii')

        assert res_data.find('dragon') != -1

    def test_delete(self, client):
        user = mixer.blend(User, email='mercury@space.com')
        pet = mixer.blend(Pet, id=153, owner=user)

        response = client.delete('/users/153/', "{}")
        check_res = client.get('/users/153/')

        assert check_res.status_code == 404