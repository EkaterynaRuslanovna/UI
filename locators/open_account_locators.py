from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class OpenAccountLocators(HeaderLocators):

    CONSUMER_NAME_SELECT = (By.CSS_SELECTOR, "select[name = 'userSelect']")
    CURRENCY_SELECT = (By.CSS_SELECTOR, "select[name = 'currency']")
    PROCESS_BUTTON = (By.CSS_SELECTOR, "button[type = 'submit']")
