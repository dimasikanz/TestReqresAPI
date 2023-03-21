import pytest
from lib.apis import APILocations
from lib.test_data import TestDataAPI

@pytest.mark.API
class TestGetUser():
    @pytest.mark.parametrize('page', TestDataAPI.PAGES_NUMBERS)
    def test_get_certain_page_of_users(self, api_client, page):
        params = {'page': page}
        response = api_client.request_advanced(method='GET', location=APILocations.USERS_LOCATION, params=params)
        page_number_from_response = response.get('page')
        data_from_page = response.get('data')
        assert page_number_from_response==page, (
            f'Неожиданный ответ, в ответе ожидался номер страницы из запроса, получено: {page_number_from_response}'
        )
        assert data_from_page is not None, f'Неожиданный ответ, в ответе ожидалось поле "data", получено: {response}'

    def test_get_certain_single_user(self, api_client, setup_valid_user):
        response = api_client.request_advanced(method='GET', location=f'{APILocations.USERS_LOCATION}/{setup_valid_user.id}')
        id_from_response = response['data']['id']
        email_from_response = response['data']['email']
        assert id_from_response==setup_valid_user.id, (
            f'Неожиданный id в ответе, ожидалось: {setup_valid_user.id}, получено: {id_from_response}'
        )
        assert email_from_response==setup_valid_user.email(
            f'Неожиданный email в ответе, ожидалось: {setup_valid_user.email}, получено: {email_from_response}'
        )

    def test_get_unknown_user(self, api_client):
        response = api_client.request_advanced(method='GET', expected_status=404,
                                               location=f'{APILocations.USERS_LOCATION}/9797979779')
        assert response == {}, f'Неожиданный ответ, ожидался пустой словарь, получено: {response}'