from .base_page import BasePage

from lib.constants import UIConstants
from lib.lib_ui import locators


class MainPage(BasePage):
    locators = locators.MainPageLocators()
    constants = UIConstants.MainPageConstants()
