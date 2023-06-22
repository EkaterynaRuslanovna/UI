import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select
from locators.consumer_locators import ConsumerLocators
import pytest
from selenium.webdriver.common.by import By
from enums.errors_enums import ErrorMassages
from allure import severity_level


@allure.story('Scope of tests "customer selector page"')
class TestConsumerSelectorPageElements:

    buttons_locator_list = [
        (ConsumerLocators.HOME_BUTTON, "HOME_BUTTON"),
        (ConsumerLocators.CONSUMER_SELECT, "CONSUMER_SELECT"),
    ]

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are visible')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, consumer_page, button_locator, test_name):

        assert consumer_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.MINOR)
    @allure.description('Checking that all LOGIN_BUTTON is not visible')
    def test_login_button_is_not_visible(self, driver, consumer_page):

        assert consumer_page.element_is_not_visible(ConsumerLocators.LOGIN_BUTTON), ErrorMassages.ELEMENT_IS_VISIBLE.value.format(ConsumerLocators.LOGIN_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are clickable')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, consumer_page, button_locator, test_name):

        assert consumer_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)

    @allure.severity(severity_level.MINOR)
    @allure.description('Checking that all elements from dropdown are clickable')
    def test_dropdown_elements_are_clickable(self, driver, consumer_page):

        with allure.step("getting options"):
            select_element = consumer_page.element_is_present(ConsumerLocators.CONSUMER_SELECT)
            select = Select(select_element)
            options = select.options

        with allure.step("assert options"):
            for option in options:
                assert consumer_page.element_is_clickable(option), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(option)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that login button is clickable')
    def test_login_button_is_clickable(self, driver, consumer_page):

        assert consumer_page.element_is_clickable(ConsumerLocators.CONSUMER_SELECT), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(ConsumerLocators.CONSUMER_SELECT)
        driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
        assert consumer_page.element_is_clickable(ConsumerLocators.CONSUMER_SELECT), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(ConsumerLocators.CONSUMER_SELECT)
        assert consumer_page.element_is_clickable(ConsumerLocators.LOGIN_BUTTON), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(ConsumerLocators.LOGIN_BUTTON)

