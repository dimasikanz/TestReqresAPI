import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lib.constants import UIConstants
from lib.lib_ui import locators


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = locators.BasePageLocators()
    constants = UIConstants.BasePageConstants()
    url = f'{constants.BASE_PAGE_URL}/'

    def is_opened(self, timeout=UIConstants.IS_OPENED_TIMEOUT_DEFAULT):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(
            f"Страница {self.url} не открылась за {timeout} секунд, текущая страница {self.driver.current_url}"
        )

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = UIConstants.WEB_DRIVER_WAIT_DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
