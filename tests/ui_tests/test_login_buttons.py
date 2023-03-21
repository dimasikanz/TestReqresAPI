import pytest
import json

@pytest.mark.ui
class TestLoginButtons:
    def test_login_successful_button_press_shows_correct_request_and_response(self, main_page, api_client):
        main_page.click_button_with_api(locator=main_page.locators.LOGIN_SUCCESSFUL_BUTTON_LOCATOR)
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_request_data = eval(main_page.find(locator=main_page.locators.OUTPUT_REQUEST_LOCATOR).text)
        ui_response_code = main_page.find(locator=main_page.locators.RESPONSE_CODE_LOCATOR)
        ui_response_dict = json.loads(main_page.find(locator=main_page.locators.RESPONSE_TEXT_LOCATOR).text)
        api_response=api_client.request_advanced(method='POST', expected_status=int(ui_response_code.text), location=ui_request_url.text,data = ui_request_data)
        assert ui_response_dict==api_response, (
            f'Неправильное тело ответа, ожидалось: {api_response}, получено: {ui_response_dict}'
        )

    def test_login_unsuccessful_button_press_shows_correct_request_and_response(self, main_page, api_client):
        main_page.click_button_with_api(locator=main_page.locators.LOGIN_UNSUCCESSFUL_BUTTON_LOCATOR)
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_request_data = eval(main_page.find(locator=main_page.locators.OUTPUT_REQUEST_LOCATOR).text)
        ui_response_code = main_page.find(locator=main_page.locators.RESPONSE_CODE_LOCATOR)
        ui_response_dict = json.loads(main_page.find(locator=main_page.locators.RESPONSE_TEXT_LOCATOR).text)
        api_response=api_client.request_advanced(method='POST', expected_status=int(ui_response_code.text), location=ui_request_url.text, data = ui_request_data)
        assert ui_response_dict==api_response, (
            f'Неправильное тело ответа, ожидалось: {api_response}, получено: {ui_response_dict}'
        )
