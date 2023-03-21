import random

import pytest

from lib.lib_api.apis import APILocations
from lib.lib_api.test_data import TestDataAPI


@pytest.mark.api
class TestOperationsWithUsers:
    @pytest.mark.parametrize("name_with_job", TestDataAPI.NAMES_WITH_JOBS)
    def test_post_for_create_user_creates_user(self, api_client, name_with_job):
        user_info = {"name": name_with_job[0], "job": name_with_job[1]}
        response = api_client.request_advanced(
            method="POST",
            expected_status=201,
            location=APILocations.USERS_LOCATION,
            data=user_info,
        )
        assert (
            response.get("id") is not None
        ), f'Неожиданный ответ, ожидалось, что в ответе будет поле "id", получено: {response}'
        assert (
            response.get("name") == user_info["name"]
        ), f'Неожиданный ответ, в поле "name" ожидалось: {user_info["name"]}, получено: {response.get("name")}'
        assert (
            response.get("job") == user_info["job"]
        ), f'Неожиданный ответ, в поле "job" ожидалось: {user_info["job"]}, получено: {response.get("job")}'

    def test_put_for_update_user_updates_user(self, api_client, setup_valid_user):
        new_user_data = {
            "name": f"new_name{random.randint(0,100000)}",
            "job": f"new_job{random.randint(0,100000)}",
        }
        response = api_client.request_advanced(
            method="PUT",
            expected_status=200,
            location=f"{APILocations.USERS_LOCATION}/{setup_valid_user.id}",
            data=new_user_data,
        )
        assert (
            response.get("name") == new_user_data["name"]
        ), f'Неожиданное значение в поле "name", ожидалось: {new_user_data["name"]}, получено: {response.get("name")}'
        assert (
            response.get("job") == new_user_data["job"]
        ), f'Неожиданное значение в поле "job", ожидалось: {new_user_data["job"]}, получено: {response.get("name")}'

    def test_patch_for_update_user_updates_user(self, api_client, setup_valid_user):
        new_user_data = {
            "name": f"new_name{random.randint(0,100000)}",
            "job": f"new_job{random.randint(0,100000)}",
        }
        response = api_client.request_advanced(
            method="PATCH",
            expected_status=200,
            location=f"{APILocations.USERS_LOCATION}/{setup_valid_user.id}",
            data=new_user_data,
        )
        assert (
            response.get("name") == new_user_data["name"]
        ), f'Неожиданное значение в поле "name", ожидалось: {new_user_data["name"]}, получено: {response.get("name")}'
        assert (
            response.get("job") == new_user_data["job"]
        ), f'Неожиданное значение в поле "job", ожидалось: {new_user_data["job"]}, получено: {response.get("name")}'

    def test_delete_user_deletes_user(self, api_client, setup_valid_user):
        response = api_client.request_advanced(
            method="DELETE",
            expected_status=204,
            jsonify=False,
            location=f"{APILocations.USERS_LOCATION}/{setup_valid_user.id}",
        )
        assert (
            response.text == ""
        ), f'Неожиданный ответ, ожидалось: "", получено: {response.text}'
