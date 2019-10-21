"""purple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from user.views import (
    UserViewSet,
    PetViewSet,
    UserList,
    UserDetail,
    PetList,
    PetDetail
    )

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'pets', PetViewSet, basename='pets')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/', csrf_exempt(UserList.as_view()), name='user-list'),
    path('users/<pk>/', csrf_exempt(UserDetail.as_view()), name='user-detail'),
    path('pets/', csrf_exempt(PetList.as_view()), name='pet-list'),
    path('pets/<pk>/', csrf_exempt(PetDetail.as_view()), name='pet-detail'),
]

