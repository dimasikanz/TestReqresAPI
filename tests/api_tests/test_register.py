import pytest
from lib.lib_api.apis import APILocations
from lib.constants import APIConstants


@pytest.mark.api
class TestRegister:
    def test_valid_register_responds_token_and_id(self, api_client):
        credentials = {
            "email": APIConstants.DEFAULT_USER_EMAIL,
            "password": APIConstants.DEFAULT_USER_PASSWORD,
        }
        response = api_client.request_advanced(
            method="POST", location=APILocations.REGISTER_LOCATION, data=credentials
        )
        assert (
            response.get("id") is not None
        ), f'Неожиданный ответ, ожидалось, что в ответе будет поле "id", получено: {response}'
        assert (
            response.get("token") is not None
        ), f'Неожиданный ответ, ожидалось, что в ответе будет поле "token", получено: {response}'

    def test_register_without_password_responds_400(self, api_client):
        credentials = {"email": APIConstants.DEFAULT_USER_EMAIL}
        response = api_client.request_advanced(
            method="POST",
            expected_status=400,
            location=APILocations.LOGIN_LOCATION,
            data=credentials,
        )
        response_error = response.get("error")
        assert (
            response_error is not None
        ), f"Неожиданный ответ, ожидалась ошибка, получено: {response}"
        assert (
            response_error == "Missing password"
        ), f"Неожиданный ответ, ожидалась ошибка Missing password, получена ошибка: {response_error}"
