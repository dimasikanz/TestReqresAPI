import pytest
from lib.lib_ui.pages.main_page import MainPage
from lib.constants import UIConstants
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

@pytest.fixture
def driver(config):
    url=config['url']
    browser=UIConstants.DEFAULT_BROWSER
    driver=get_driver(browser_name=browser, url=url)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

def get_driver(browser_name,
               url):
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(
                    version=UIConstants.DRIVER_VERSION
                ).install()
            )
        )
    else:
        raise RuntimeError(f'Браузер не поддерживается: "{browser_name}"')
    driver.get(url)
    driver.maximize_window()
    return driver
