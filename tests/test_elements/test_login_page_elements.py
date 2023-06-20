from locators.login_page_locators import LoginPageLocators
import pytest
from enums.errors_enums import ErrorMassages


class TestMainPageElements:

    buttons_locator_list = [
        (LoginPageLocators.HOME_BUTTON, "HOME_BUTTON"),
        (LoginPageLocators.CONSUMER_LOGIN_BUTTON, "CONSUMER_LOGIN_BUTTON"),
        (LoginPageLocators.MANAGER_LOGIN_BUTTON, "MANAGER_LOGIN_BUTTON"),
        ]

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, login_page, button_locator, test_name):
        """
        Checking that all elements are visible
        :param driver: fixture
        :param login_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
        """
        assert login_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, login_page, button_locator, test_name):
        """
        Checking that all elements are clickable
        :param driver: fixture
        :param login_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        assert login_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)
