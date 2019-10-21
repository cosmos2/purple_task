import json
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import User, Pet
from .serializers import UserSerializer, PetSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_value_regex = '[^/]+'  # DefaultRouter()에서 마침표를 매칭 못해서 따로 이곳에서 설정해줘야 함.
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        owner = self.request.query_params.get('owner', None)

        if owner:
            owner = User.objects.get(pk=owner)

        if self.request.query_params.get('rep') == 'true':
            rep = True
        else:
            rep = False

        if owner and rep is True:
            pets = Pet.objects.filter(owner=owner, representative=rep)
        elif owner and rep is False:
            pets = Pet.objects.filter(owner=owner)
        else:
            pets = Pet.objects.all()
        return pets

class UserList(ListView):
    model = User

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user = User.objects.create(**data)
        return HttpResponse(user)


class UserDetail(DetailView):
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user = User.objects.filter(pk=kwargs['pk'])
        user.update(**data)
        return render(request, 'user/user_detail.html', {'object': user[0]})

    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user = User.objects.filter(pk=kwargs['pk'])
        user.delete()
        return HttpResponse(f"{kwargs['pk']} user is deleted")


class PetList(ListView):
    model = Pet

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        pet = Pet.objects.create(**data)
        return HttpResponse(pet)

class PetDetail(DetailView):
    queryset = Pet.objects.all()

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        pet = Pet.objects.filter(pk=kwargs['pk'])
        pet.update(**data)
        return render(request, 'user/pet_detail.html', {'object': pet[0]})

    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        pet = Pet.objects.filter(pk=kwargs['pk'])
        pet.delete()
        return HttpResponse(f"{kwargs['pk']} pet is deleted")