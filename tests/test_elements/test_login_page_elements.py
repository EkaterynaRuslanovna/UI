import allure
from allure_commons.types import AttachmentType
from locators.login_page_locators import LoginPageLocators
import pytest
from enums.errors_enums import ErrorMassages
from allure import severity_level


@allure.story('Scope of tests "login page"')
class TestMainPageElements:
    buttons_locator_list = [
        (LoginPageLocators.HOME_BUTTON, "HOME_BUTTON"),
        (LoginPageLocators.CONSUMER_LOGIN_BUTTON, "CONSUMER_LOGIN_BUTTON"),
        (LoginPageLocators.MANAGER_LOGIN_BUTTON, "MANAGER_LOGIN_BUTTON"),
    ]

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are visible')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, login_page, button_locator, test_name):

        assert login_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.CRITICAL)
    @allure.description('Checking that all elements are clickable')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, login_page, button_locator, test_name):

        assert login_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)
