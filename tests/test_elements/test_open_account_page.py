from selenium.webdriver.support.ui import Select
from locators.open_account_locators import OpenAccountLocators
import pytest
from selenium.webdriver.common.by import By
from enums.errors_enums import ErrorMassages


class TestOpenAccountPageElements:

    buttons_locator_list = [
        (OpenAccountLocators.HOME_BUTTON, "HOME_BUTTON"),
        (OpenAccountLocators.CONSUMER_NAME_SELECT, "CONSUMER_NAME_SELECT"),
        (OpenAccountLocators.CURRENCY_SELECT, "CURRENCY_SELECT"),
        (OpenAccountLocators.PROCESS_BUTTON, "PROCESS_BUTTON"),
    ]

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, open_account_page, button_locator, test_name):
        """
        Checking that all elements are visible
        :param driver: fixture
        :param open_account_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
        """
        assert open_account_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)

    def test_dropdown_consumer_elements_are_clickable(self, driver, open_account_page):
        """
        Checking that all elements from dropdown are clickable
        :param driver: fixture
        :param open_account_page: fixture
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        select_element = open_account_page.element_is_present(OpenAccountLocators.CONSUMER_NAME_SELECT)
        select = Select(select_element)
        options = select.options

        for option in options:
            assert open_account_page.element_is_clickable(option), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(option)

    def test_dropdown_currency_elements_are_clickable(self, driver, open_account_page):
        """
        Checking that all elements from dropdown are clickable
        :param driver: fixture
        :param open_account_page: fixture
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        select_element = open_account_page.element_is_present(OpenAccountLocators.CURRENCY_SELECT)
        select = Select(select_element)
        options = select.options

        for option in options:
            assert open_account_page.element_is_clickable(option), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(option)

    def test_open_account(self, driver, open_account_page):
        """
        Checking flow to open account
        :param driver: fixture
        :param open_account_page: fixture
        :return: If the account did not create, an error FAILED_TO_OPEN_ACCOUNT is returned
                 If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
                 If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        assert open_account_page.element_is_clickable(OpenAccountLocators.CONSUMER_NAME_SELECT), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(OpenAccountLocators.CONSUMER_NAME_SELECT)
        driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()

        assert open_account_page.element_is_clickable(OpenAccountLocators.CURRENCY_SELECT), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(OpenAccountLocators.CURRENCY_SELECT)
        driver.find_element(By.CSS_SELECTOR, "option[value='Dollar']").click()

        assert open_account_page.element_is_clickable(OpenAccountLocators.PROCESS_BUTTON), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(OpenAccountLocators.PROCESS_BUTTON)
        driver.find_element(By.CSS_SELECTOR, ".ng-dirty > button").click()

        assert "Account created successfully with account Number :" in driver.switch_to.alert.text, ErrorMassages.FAILED_TO_OPEN_ACCOUNT.value
