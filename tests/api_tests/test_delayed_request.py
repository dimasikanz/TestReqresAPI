import pytest
from lib.test_data import TestDataAPI
from lib.apis import APILocations
from datetime import datetime, timedelta

@pytest.mark.API
class TestGetUsers:
    def test_get_page_of_users_responds_correct_fields(self, api_client):
        params = {"delay": 3}
        response = api_client.request_advanced(
            method="GET", location=APILocations.USERS_LOCATION, params=params
        )
        page_number_from_response = response.get("page")
        data_from_page = response.get("data")
        assert (
            page_number_from_response is not None
        ), f"Неожиданный ответ, в поле 'page' ожидалось не None, получено: {page_number_from_response}"
        assert (
            data_from_page is not None
        ), f"Неожиданный ответ, в поле 'data' ожидалось не None, получено: {data_from_page}"

    @pytest.mark.parametrize("delay", TestDataAPI.DELAYS)
    def test_get_page_of_users_with_delay_responds_with_correct_delay(self, api_client, delay):
        """Тест, проверяющий, что запрос с задержкой выжидает нужную задержку. Нет требований, какое отклонение от
        задержки допустимо, поэтому проверка будет проводиться на соответствие задержки с максимальным отклонением в
         1 секунду"""
        params = {"delay": delay}
        start_time=datetime.now()
        api_client.request_advanced(
            method="GET", location=APILocations.USERS_LOCATION, params=params
        )
        end_time=datetime.now()
        assert (end_time-start_time>timedelta(seconds=delay-1)) and (end_time-start_time<timedelta(seconds=delay+1))