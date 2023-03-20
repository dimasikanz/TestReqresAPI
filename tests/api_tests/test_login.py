import pytest
from lib.apis import APILocations
from lib.test_data import CommonTestData


@pytest.mark.API
class TestLogin():
    def test_valid_login(self, api_client, setup_valid_user_credentials):
        credentials = {"email": setup_valid_user_credentials.email,
                       "password": setup_valid_user_credentials.password}
        response = api_client.request_advanced(method='POST', location=APILocations.LOGIN_LOCATION, data=credentials)
        assert response.get('token') is not None, (
            f'Неожиданный ответ, ожидалось, что в ответе будет поле "token", получено: {response}'
        )

    def test_login_without_password(self, api_client, setup_valid_user_credentials):
        credentials = {"email": setup_valid_user_credentials.email}
        response = api_client.request_advanced(method='POST', expected_status=400,
                                               location=APILocations.LOGIN_LOCATION, data=credentials)
        response_error = response.get('error')
        assert response_error is not None, (
            f'Неожиданный ответ, ожидалась ошибка, получено: {response}'
        )
        assert response_error == 'Missing password', (
            f'Неожиданный ответ, ожидалась ошибка Missing password, получена ошибка: {response_error}'
        )