from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class LoginPageLocators(HeaderLocators):

    CONSUMER_LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-primary btn-lg'][1]")
    MANAGER_LOGIN_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")

