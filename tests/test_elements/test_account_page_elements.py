import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locators.account_locators import AccountLocators
import pytest
from enums.errors_enums import ErrorMassages


class TestAccountPageElements:

    buttons_locator_list = [
        (AccountLocators.HOME_BUTTON, "HOME_BUTTON"),
        (AccountLocators.CONSUMER_LOGOUT_BUTTON, "CONSUMER_LOGOUT_BUTTON"),
        (AccountLocators.ACCOUNT_SELECT, "ACCOUNT_SELECT"),
        (AccountLocators.TRANSACTIONS_BUTTON, "TRANSACTIONS_BUTTON"),
        (AccountLocators.DEPOSIT_BUTTON, "DEPOSIT_BUTTON"),
        (AccountLocators.WITHDRAW_BUTTON, "WITHDRAW_BUTTON"),
    ]

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, account_page, button_locator, test_name):
        """
        Checking that all elements are visible
        :param driver: fixture
        :param account_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
        """
        assert account_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)

    def test_dropdown_elements_are_clickable(self, driver, account_page):
        """
        Checking that all elements from dropdown are clickable
        :param driver: fixture
        :param account_page: fixture
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        select_element = account_page.element_is_present(AccountLocators.ACCOUNT_SELECT)
        select = Select(select_element)
        options = select.options

        for option in options:
            assert account_page.element_is_clickable(option), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(option)

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, account_page, button_locator, test_name):
        """
        Checking that all elements are clickable
        :param driver: fixture
        :param account_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        assert account_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)

    def test_input_deposit_is_visible(self, driver, account_page):
        """
        Checking that input deposit is visible
        :param driver: fixture
        :param account_page: fixture
        :return: If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
        """
        driver.find_element(*AccountLocators.DEPOSIT_BUTTON).click()
        assert account_page.element_is_visible(AccountLocators.DEPOSIT_INPUT), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(AccountLocators.DEPOSIT_INPUT)
        assert account_page.element_is_visible(AccountLocators.DEPOSIT_SUBMIT_BUTTON), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(AccountLocators.DEPOSIT_SUBMIT_BUTTON)

    def test_input_withdraw_is_visible(self, driver, account_page):
        """
        Checking that input withdraw is visible
        :param driver: fixture
        :param account_page: fixture
        :return: If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
        """
        driver.find_element(*AccountLocators.WITHDRAW_BUTTON).click()
        assert account_page.element_is_visible(AccountLocators.WITHDRAW_INPUT), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(AccountLocators.WITHDRAW_INPUT)
        assert account_page.element_is_visible(AccountLocators.WITHDRAW_SUBMIT_BUTTON), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(AccountLocators.WITHDRAW_SUBMIT_BUTTON)

    def test_fill_deposit(self, driver, account_page):
        """
        Checking flow to make deposit
        :param driver: fixture
        :param account_page: fixture
        :return: If the balance did not match, an error CURRENT_BALANCE_IS_NOT_EQL is returned
        """
        account_page.element_is_clickable(AccountLocators.DEPOSIT_BUTTON).click()
        current_balance = driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
        current_balance = current_balance[1].text
        deposit = account_page.fill_amount_deposit()
        new_balance = driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
        new_balance = new_balance[1].text
        assert int(new_balance) == int(current_balance) + int(deposit), ErrorMassages.CURRENT_BALANCE_IS_NOT_EQL.value.format(new_balance, current_balance + deposit)

    def test_fill_withdraw(self, driver, account_page):
        """
        Checking flow to make withdraw
        :param driver: fixture
        :param account_page: fixture
        :return: If the balance did not match, an error CURRENT_BALANCE_IS_NOT_EQL is returned
        """
        account_page.element_is_clickable(AccountLocators.WITHDRAW_BUTTON).click()
        current_balance = driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
        current_balance = current_balance[1].text
        time.sleep(2)
        withdraw = account_page.fill_amount_withdraw()
        new_balance = driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
        new_balance = new_balance[1].text
        assert int(new_balance) == int(current_balance) - int(withdraw), ErrorMassages.CURRENT_BALANCE_IS_NOT_EQL.value.format(new_balance, current_balance - withdraw)
