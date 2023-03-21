from .apiclient import ApiClient
from lib.apis import APILocations
from lib.constants import CommonConstants


def create_new_account(
    api_client: ApiClient,
    email=CommonConstants.DEFAULT_USER_EMAIL,
    password=CommonConstants.DEFAULT_USER_PASSWORD,
):
    data = {"email": email, "password": password}
    response = api_client.request_advanced(
        method="POST", location=APILocations.REGISTER_LOCATION, data=data
    )
    return {"id": response["id"], "token": response["token"]}


def create_new_user(
    api_client: ApiClient,
    name=CommonConstants.DEFAULT_USER_NAME,
    job=CommonConstants.DEFAULT_USER_JOB,
):
    data = {"name": name, "job": job}
    response = api_client.request_advanced(
        method="POST",
        expected_status=201,
        location=APILocations.USERS_LOCATION,
        data=data,
    )
    return {"name": response["id"], "job": response["job"], "id": response["id"]}
