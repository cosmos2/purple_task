from django.test import Client
from rest_framework.test import APIClient
import pytest


@pytest.fixture(scope='session', autouse=True)
def client():
    client = Client()
    return client

@pytest.fixture(scope='session', autouse=True)
def api_client():
    apiclient = APIClient()
    return apiclient