from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class ManagerLocators(HeaderLocators):

    ADD_CONSUMER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.tab[ng-click='addCust()']")
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.tab[ng-click='openAccount()']")
    CONSUMERS_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.tab[ng-click='showCust()']")
