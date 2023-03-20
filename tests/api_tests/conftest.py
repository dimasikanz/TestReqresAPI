import random

import pytest

from api.apiclient import ApiClient
from api.supporting_requests import create_new_user
from lib.constants import CommonConstants
from lib.dataclasses.setup_dataclasses import NewUserData
from lib.dataclasses.builders_dataclasses import Builder

def pytest_addoption(parser):
    """Парсер для чтения параметров из консоли"""
    parser.addoption("--url", default=CommonConstants.DEFAULT_URL)


@pytest.fixture(scope="session")
def config(request):
    """
    Вынос спарсенных из консоли параметров в словарь "config"
    """
    url = request.config.getoption("--url")

    return {
        "url": url
    }


@pytest.fixture(scope="session")
def api_client(config):
    return ApiClient(
        base_url=config["url"]
    )


@pytest.fixture(scope="session")
def builder():
    return Builder()

@pytest.fixture()
def setup_valid_user_credentials(api_client):
    email = CommonConstants.DEFAULT_USER_EMAIL
    password = CommonConstants.DEFAULT_USER_PASSWORD
    register_data = create_new_user(api_client=api_client, email=email, password=password)
    return NewUserData(email=email, password=password, id=register_data['id'], token=register_data['token'])
