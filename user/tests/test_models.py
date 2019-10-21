import pytest
import json
from datetime import datetime
from mixer.backend.django import mixer
from user.models import User, Pet

@pytest.mark.django_db
class TestModel:

    def test_create_user(self):
        user = mixer.blend(
            User,
            email='pengsoo@.antarctic.com',
            name='pengsoo',
            phone='010-1234-5678',
            zipcode='12345',
            address='antarctic, earth',
            address_detail='King Sejong Station',
            role='SU'
            )
        assert user.email == 'pengsoo@.antarctic.com'
        assert user.name == 'pengsoo'
        assert user.phone == '010-1234-5678'
        assert user.zipcode == '12345'
        assert user.address == 'antarctic, earth'
        assert user.address_detail == 'King Sejong Station'
        assert user.role == 'SU'

    def test_update_user(self):
        user = mixer.blend(
            User,
            email='pengsoo@antarctic.com',
            name='pengsoo'
        )
        

    def test_create_pet(self):
        user = mixer.blend(User, email='pengsoo@.antarctic.com')
        date = datetime.now().date()
        illness = json.dumps({'fin': 'broken'})
        allergy = json.dumps({'type': None})
        prefer_ingredient = json.dumps({'prefer': 'omega3'})

        pet = mixer.blend(
            Pet,
            owner=user,
            name='orca',
            photo='http://something.com/orca.jpg',
            birth=date,
            register_num='0001',
            illness=illness,
            allergy=allergy,
            prefer_ingredient=prefer_ingredient,
            representative=False
        )

        assert pet.owner == user
        assert pet.name == 'orca'
        assert pet.photo == 'http://something.com/orca.jpg'
        assert pet.birth == date
        assert pet.register_num == '0001'
        assert pet.illness == illness
        assert pet.allergy == allergy
        assert pet.prefer_ingredient == prefer_ingredient
        assert pet.representative == False

    def test_only_one_representative_pet(self):
        user = mixer.blend(User)
        with pytest.raises(Exception):
            pet_1 = mixer.blend(Pet, owner=user, representative=True)
            assert mixer.blend(Pet, owner=user, representative=True)
