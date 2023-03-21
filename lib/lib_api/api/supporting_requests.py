from lib.constants import APIConstants
from lib.lib_api.apis import APILocations

from .apiclient import ApiClient


def create_new_account(
    api_client: ApiClient,
    email=APIConstants.DEFAULT_USER_EMAIL,
    password=APIConstants.DEFAULT_USER_PASSWORD,
):
    data = {"email": email, "password": password}
    response = api_client.request_advanced(
        method="POST", location=APILocations.REGISTER_LOCATION, data=data
    )
    return {"id": response["id"], "token": response["token"]}


def create_new_user(
    api_client: ApiClient,
    name=APIConstants.DEFAULT_USER_NAME,
    job=APIConstants.DEFAULT_USER_JOB,
):
    data = {"name": name, "job": job}
    response = api_client.request_advanced(
        method="POST",
        expected_status=201,
        location=APILocations.USERS_LOCATION,
        data=data,
    )
    return {"name": response["id"], "job": response["job"], "id": response["id"]}
