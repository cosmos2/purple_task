from django.contrib.postgres.fields import JSONField
from django.core.exceptions import FieldError
from django.db import models


class User(models.Model):
    SUPER_USER = 'SU'
    GENERAL_USER = 'GU'
    STAFF = 'ST'
    ROLE_CHOICES = [
        (SUPER_USER, 'Super_user'),
        (GENERAL_USER, 'General_user'),
        (STAFF, 'Staff')
    ]

    email = models.EmailField(max_length=254, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    address_detail = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=GENERAL_USER,
    )

    def __str__(self):
        return self.name


class Pet(models.Model):
    DOG = 'D'
    CAT = 'C'
    ETC = 'E'
    SPECISE_CHOICES = [
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (ETC, 'Etc')
    ]
    species = models.CharField(
        max_length=1,
        choices=SPECISE_CHOICES,
        null=True,
        blank=True
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.URLField(max_length=255, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    register_num = models.CharField(max_length=15, null=True, blank=True)
    illness = JSONField(null=True, blank=True)
    allergy = JSONField(null=True, blank=True)
    prefer_ingredient = JSONField(null=True, blank=True)
    representative = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        대표 반려동물을 1마리만 선택할 수 있는 로직.
        """
        pets = self.owner.pet_set.all()

        for pet in pets:
            if pet.representative is True and self.representative is True:
                if pet == self:
                    break
                else:
                    raise Exception("Already have representative pet")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name