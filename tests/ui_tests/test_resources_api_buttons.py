import pytest
import json

@pytest.mark.ui
class TestResourcesButtons:
    def test_list_resources_button_press_shows_correct_request_and_response(self, main_page, api_client):
        main_page.click_button_with_api(locator=main_page.locators.LIST_RESOURCES_BUTTON_LOCATOR)
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_response_code = main_page.find(locator=main_page.locators.RESPONSE_CODE_LOCATOR)
        ui_response_dict = json.loads(main_page.find(locator=main_page.locators.RESPONSE_TEXT_LOCATOR).text)
        api_response=api_client.request_advanced(method='GET', expected_status=int(ui_response_code.text), location=ui_request_url.text)
        assert ui_response_dict==api_response, (
            f'Неправильное тело ответа, ожидалось: {api_response}, получено: {ui_response_dict}'
        )

    def test_single_resource_button_press_shows_correct_request_and_response(self, main_page, api_client):
        main_page.click_button_with_api(locator=main_page.locators.SINGLE_RESOURCE_BUTTON_LOCATOR)
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_response_code = main_page.find(locator=main_page.locators.RESPONSE_CODE_LOCATOR)
        ui_response_dict = json.loads(main_page.find(locator=main_page.locators.RESPONSE_TEXT_LOCATOR).text)
        api_response=api_client.request_advanced(method='GET', expected_status=int(ui_response_code.text), location=ui_request_url.text)
        assert ui_response_dict==api_response, (
            f'Неправильное тело ответа, ожидалось: {api_response}, получено: {ui_response_dict}'
        )


    def test_single_resource_not_found_button_press_shows_correct_request_and_response(self, main_page, api_client):
        main_page.click_button_with_api(locator=main_page.locators.SINGLE_RESOURCE_NOT_FOUND_BUTTON_LOCATOR)
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_response_code = main_page.find(locator=main_page.locators.RESPONSE_CODE_LOCATOR)
        ui_response = main_page.find(locator=main_page.locators.RESPONSE_TEXT_LOCATOR).text
        api_response=api_client.request_advanced(method='GET', jsonify=False, expected_status=int(ui_response_code.text), location=ui_request_url.text)
        assert ui_response==api_response.text, (
            f'Неправильное тело ответа, ожидалось: {api_response.text}, получено: {ui_response}'
        )