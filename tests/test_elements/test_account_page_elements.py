import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locators.account_locators import AccountLocators
import pytest
from enums.errors_enums import ErrorMassages
from allure import severity_level


@allure.story('Scope of tests "account page"')
class TestAccountPageElements:

    buttons_locator_list = [
        (AccountLocators.HOME_BUTTON, "HOME_BUTTON"),
        (AccountLocators.CONSUMER_LOGOUT_BUTTON, "CONSUMER_LOGOUT_BUTTON"),
        (AccountLocators.ACCOUNT_SELECT, "ACCOUNT_SELECT"),
        (AccountLocators.TRANSACTIONS_BUTTON, "TRANSACTIONS_BUTTON"),
        (AccountLocators.DEPOSIT_BUTTON, "DEPOSIT_BUTTON"),
        (AccountLocators.WITHDRAW_BUTTON, "WITHDRAW_BUTTON"),
    ]

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are visible')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, account_page, button_locator, test_name):

        assert account_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements from dropdown are clickable')
    def test_dropdown_elements_are_clickable(self, driver, account_page):

        with allure.step("getting options"):
            select_element = account_page.element_is_present(AccountLocators.ACCOUNT_SELECT)
            select = Select(select_element)
            options = select.options

        with allure.step("assert options"):
            for option in options:
                assert account_page.element_is_clickable(option), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(option)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are clickable')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, account_page, button_locator, test_name):

        assert account_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that input deposit is visible')
    def test_input_deposit_is_visible(self, driver, account_page):

        driver.find_element(*AccountLocators.DEPOSIT_BUTTON).click()
        assert account_page.element_is_visible(AccountLocators.DEPOSIT_INPUT), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(AccountLocators.DEPOSIT_INPUT)
        assert account_page.element_is_visible(AccountLocators.DEPOSIT_SUBMIT_BUTTON), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(AccountLocators.DEPOSIT_SUBMIT_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that input withdraw is visible')
    def test_input_withdraw_is_visible(self, driver, account_page):

        driver.find_element(*AccountLocators.WITHDRAW_BUTTON).click()
        assert account_page.element_is_visible(AccountLocators.WITHDRAW_INPUT), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(AccountLocators.WITHDRAW_INPUT)
        assert account_page.element_is_visible(AccountLocators.WITHDRAW_SUBMIT_BUTTON), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(AccountLocators.WITHDRAW_SUBMIT_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.CRITICAL)
    @allure.description('Checking flow to make deposit')
    def test_fill_deposit(self, driver, account_page):

        with allure.step("previous balance"):
            account_page.element_is_clickable(AccountLocators.DEPOSIT_BUTTON).click()
            current_balance = driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
            current_balance = current_balance[1].text
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        with allure.step("current balance"):
            deposit = account_page.fill_amount_deposit()
            new_balance = driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
            new_balance = new_balance[1].text
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        assert int(new_balance) == int(current_balance) + int(deposit), ErrorMassages.CURRENT_BALANCE_IS_NOT_EQL.value.format(new_balance, current_balance + deposit)

    @allure.severity(severity_level.CRITICAL)
    @allure.description('Checking flow to make withdraw')
    def test_fill_withdraw(self, driver, account_page):

        with allure.step("previous balance"):
            account_page.element_is_clickable(AccountLocators.WITHDRAW_BUTTON).click()
            current_balance = driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
            current_balance = current_balance[1].text
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        with allure.step("current balance"):
            withdraw = account_page.fill_amount_withdraw()
            new_balance = driver.find_elements(By.CSS_SELECTOR, "div.center strong.ng-binding")
            new_balance = new_balance[1].text
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

        assert int(new_balance) == int(current_balance) - int(withdraw), ErrorMassages.CURRENT_BALANCE_IS_NOT_EQL.value.format(new_balance, current_balance - withdraw)
