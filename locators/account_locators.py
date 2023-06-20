from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators


class AccountLocators(HeaderLocators):

    ACCOUNT_SELECT = (By.CSS_SELECTOR, "select[id='accountSelect']")
    TRANSACTIONS_BUTTON = (By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-lg') and contains(@class, 'tab') and @ng-click='transactions()']")
    DEPOSIT_BUTTON = (By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-lg') and contains(@class, 'tab') and @ng-click='deposit()']")
    WITHDRAW_BUTTON = (By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-lg') and contains(@class, 'tab') and @ng-click='withdrawl()']")

    DEPOSIT_INPUT = (By.XPATH, "//input[@placeholder='amount']")
    DEPOSIT_SUBMIT_BUTTON = (By.XPATH, "//button[@class='btn btn-default']")

    WITHDRAW_INPUT = (By.XPATH, "//input[@placeholder='amount']")
    WITHDRAW_SUBMIT_BUTTON = (By.XPATH, "//button[@class='btn btn-default']")

