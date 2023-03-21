from selenium.webdriver.support import expected_conditions as EC

from lib.constants import UIConstants
from lib.lib_ui import locators

from .base_page import BasePage


class MainPage(BasePage):
    locators = locators.MainPageLocators()
    constants = UIConstants.MainPageConstants()

    def click_button_with_api(self, locator, timeout=None):
        """
        Метод для нажатия на кнопку с api. Ожидание смены url`a запроса необходимо всвязи с задержкой при прогрузке
        после нажатия на кнопку. (Запрос и ответ к нему загружаются с определенной задержкой)
        """
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        start_request_url = self.find(self.locators.URL_LOCATOR).text
        current_url = self.find(self.locators.URL_LOCATOR).text
        elem.click()
        if elem != self.wait(timeout).until(
            EC.element_to_be_clickable(self.locators.DEFAULT_PRESSED_BUTTON_LOCATOR)
        ):
            while start_request_url == current_url:
                current_url = self.find(self.locators.URL_LOCATOR).text
        # Ожидание прокрутки "Спиннера" (Отправка запроса -> получение ответа)
        self.wait(timeout).until(
            EC.presence_of_element_located(self.locators.HIDDEN_SPINNER_LOCATOR)
        )
