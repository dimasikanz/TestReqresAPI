import pytest

from lib.lib_api.apis import APILocations


@pytest.mark.api
class TestGetResources:
    def test_get_page_of_recources_responds_correct_response(self, api_client):
        response = api_client.request_advanced(
            method="GET", location=APILocations.RESOURCES_LOCATION
        )
        page_number_from_response = response.get("page")
        data_from_page = response.get("data")
        assert (
            page_number_from_response == 1
        ), f"Неожиданный ответ, в ответе ожидался номер страницы 1, получено: {page_number_from_response}"
        assert (
            data_from_page is not None
        ), f'Неожиданный ответ, в ответе ожидалось поле "data", получено: {response}'

    def test_get_certain_recource_responds_correct_response(
        self, api_client, setup_valid_account
    ):
        request_resource_id = 2
        response = api_client.request_advanced(
            method="GET",
            location=f"{APILocations.RESOURCES_LOCATION}/{request_resource_id}",
        )
        id_from_response = response["data"]["id"]
        assert (
            id_from_response == request_resource_id
        ), f"Неожиданный id в ответе, ожидалось: {request_resource_id}, получено: {id_from_response}"

    def test_get_nonexistent_resouce_responds_correct_response(self, api_client):
        response = api_client.request_advanced(
            method="GET",
            expected_status=404,
            location=f"{APILocations.RESOURCES_LOCATION}/9797979779",
        )
        assert (
            response == {}
        ), f"Неожиданный ответ, ожидался пустой словарь, получено: {response}"
