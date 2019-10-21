from rest_framework import serializers
from .models import User, Pet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = (
            '__all__'
        )


class PetSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()

    class Meta:
        model = Pet

        fields = (
            '__all__'
        )