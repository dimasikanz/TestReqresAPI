import pytest

from lib.lib_api.api.apiclient import ApiClient
from lib.lib_api.api.supporting_requests import create_new_account, create_new_user
from lib.constants import APIConstants
from lib.lib_api.dataclasses.setup_dataclasses import NewUserData, NewAccountData

@pytest.fixture(scope="session")
def api_client(config):
    return ApiClient(base_url=config["url"])


@pytest.fixture()
def setup_valid_account(api_client):
    email = APIConstants.DEFAULT_USER_EMAIL
    password = APIConstants.DEFAULT_USER_PASSWORD
    register_data = create_new_account(
        api_client=api_client, email=email, password=password
    )
    return NewAccountData(
        email=email,
        password=password,
        id=register_data["id"],
        token=register_data["token"],
    )


@pytest.fixture()
def setup_valid_user(api_client):
    name = APIConstants.DEFAULT_USER_NAME
    job = APIConstants.DEFAULT_USER_JOB
    user_data = create_new_user(api_client=api_client, name=name, job=job)
    return NewUserData(name=user_data["name"], job=user_data["job"], id=user_data["id"])
