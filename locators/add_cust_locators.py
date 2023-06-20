from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class AddCustLocators(HeaderLocators):

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model = 'fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model = 'lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model = 'postCd']")
    ADD_CONSUMER_BUTTON = (By.CSS_SELECTOR, "button[type = 'submit']")
