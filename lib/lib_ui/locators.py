from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class MainPageLocators:
    LIST_USERS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='users']")
    SINGLE_USER_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='users-single']")
    SINGLE_USER_NOT_FOUND_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "[data-id='users-single-not-found']",
    )
    LIST_RESOURCES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='unknown']")
    SINGLE_RESOURCE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='unknown-single']")
    SINGLE_RESOURCE_NOT_FOUND_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "[data-id='unknown-single-not-found']",
    )
    CREATE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='post']")
    UPDATE_PUT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='put']")
    UPDATE_PATCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='patch']")
    DELETE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='delete']")
    REGISTER_SUCCESSFUL_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "[data-id='register-successful']",
    )
    REGISTER_UNSUCCESSFUL_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "[data-id='register-unsuccessful']",
    )
    LOGIN_SUCCESSFUL_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='login-successful']")
    LOGIN_UNSUCCESSFUL_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        "[data-id='login-unsuccessful']",
    )
    DELAYED_RESPONSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='delay']")
    RESPONSE_CODE_LOCATOR = (By.CLASS_NAME, "response-code")
    RESPONSE_TEXT_LOCATOR = (By.CSS_SELECTOR, "[data-key='output-response']")
    URL_LOCATOR = (By.CLASS_NAME, "url")
    OUTPUT_REQUEST_LOCATOR = (By.CSS_SELECTOR, '[data-key="output-request"]')
    DEFAULT_PRESSED_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-id='users']")
    HIDDEN_SPINNER_LOCATOR = (By.CSS_SELECTOR, ".spinner[hidden='true']")
