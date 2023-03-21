import json

import pytest


@pytest.mark.ui
class TestOperationsWithUsersButtons:
    def test_create_button_press_shows_correct_request_and_response(
        self, main_page, api_client
    ):
        main_page.click_button_with_api(
            locator=main_page.locators.CREATE_BUTTON_LOCATOR
        )
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_request_data = eval(
            main_page.find(locator=main_page.locators.OUTPUT_REQUEST_LOCATOR).text
        )
        ui_response_code = main_page.find(
            locator=main_page.locators.RESPONSE_CODE_LOCATOR
        )
        ui_response_dict = json.loads(
            main_page.find(locator=main_page.locators.RESPONSE_TEXT_LOCATOR).text
        )
        api_response = api_client.request_advanced(
            method="POST",
            expected_status=int(ui_response_code.text),
            location=ui_request_url.text,
            data=ui_request_data,
        )
        ui_response_dict.pop("id")
        ui_response_dict.pop("createdAt")
        api_response.pop("id")
        api_response.pop("createdAt")
        assert (
            ui_response_dict == api_response
        ), f"Неправильное тело ответа, ожидалось: {api_response}, получено: {ui_response_dict}"

    def test_update_put_button_press_shows_correct_request_and_response(
        self, main_page, api_client
    ):
        main_page.click_button_with_api(
            locator=main_page.locators.UPDATE_PUT_BUTTON_LOCATOR
        )
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_request_data = eval(
            main_page.find(locator=main_page.locators.OUTPUT_REQUEST_LOCATOR).text
        )
        ui_response_code = main_page.find(
            locator=main_page.locators.RESPONSE_CODE_LOCATOR
        )
        ui_response_dict = json.loads(
            main_page.find(locator=main_page.locators.RESPONSE_TEXT_LOCATOR).text
        )
        api_response = api_client.request_advanced(
            method="PUT",
            expected_status=int(ui_response_code.text),
            location=ui_request_url.text,
            data=ui_request_data,
        )
        ui_response_dict.pop("updatedAt")
        api_response.pop("updatedAt")
        assert (
            ui_response_dict == api_response
        ), f"Неправильное тело ответа, ожидалось: {api_response}, получено: {ui_response_dict}"

    def test_update_patch_button_press_shows_correct_request_and_response(
        self, main_page, api_client
    ):
        main_page.click_button_with_api(
            locator=main_page.locators.UPDATE_PATCH_BUTTON_LOCATOR
        )
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_request_data = eval(
            main_page.find(locator=main_page.locators.OUTPUT_REQUEST_LOCATOR).text
        )
        ui_response_code = main_page.find(
            locator=main_page.locators.RESPONSE_CODE_LOCATOR
        )
        ui_response_dict = json.loads(
            main_page.find(locator=main_page.locators.RESPONSE_TEXT_LOCATOR).text
        )
        api_response = api_client.request_advanced(
            method="PATCH",
            expected_status=int(ui_response_code.text),
            location=ui_request_url.text,
            data=ui_request_data,
        )
        ui_response_dict.pop("updatedAt")
        api_response.pop("updatedAt")
        assert (
            ui_response_dict == api_response
        ), f"Неправильное тело ответа, ожидалось: {api_response}, получено: {ui_response_dict}"

    def test_delete_button_press_shows_correct_request_and_response(
        self, main_page, api_client
    ):
        main_page.click_button_with_api(
            locator=main_page.locators.DELETE_BUTTON_LOCATOR
        )
        ui_request_url = main_page.find(locator=main_page.locators.URL_LOCATOR)
        ui_response_code = main_page.find(
            locator=main_page.locators.RESPONSE_CODE_LOCATOR
        )
        ui_response = main_page.find(
            locator=main_page.locators.RESPONSE_TEXT_LOCATOR
        ).text
        api_response = api_client.request_advanced(
            method="DELETE",
            jsonify=False,
            expected_status=int(ui_response_code.text),
            location=ui_request_url.text,
        )
        assert (
            ui_response == api_response.text
        ), f"Неправильное тело ответа, ожидалось: {api_response.text}, получено: {ui_response}"
