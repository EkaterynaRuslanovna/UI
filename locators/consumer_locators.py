from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class ConsumerLocators(HeaderLocators):

    CONSUMER_SELECT = (By.CSS_SELECTOR, "#userSelect")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-default")
