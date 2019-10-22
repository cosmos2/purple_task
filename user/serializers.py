from rest_framework import serializers

from .models import User, Pet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = (
            'email',
            'name',
            'phone',
            'zipcode',
            'address',
            'address_detail',
            'role'
        )


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet

        fields = (
            'owner',
            'name',
            'photo',
            'birth',
            'register_num',
            'illness',
            'allergy',
            'prefer_ingredient',
            'representative'
        )