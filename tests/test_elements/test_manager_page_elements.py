from locators.manager_locators import ManagerLocators
import pytest
from enums.errors_enums import ErrorMassages


class TestManagerPageElements:

    buttons_locator_list = [
        (ManagerLocators.HOME_BUTTON, "HOME_BUTTON"),
        (ManagerLocators.ADD_CONSUMER_BUTTON, "ADD_CONSUMER_BUTTON"),
        (ManagerLocators.OPEN_ACCOUNT_BUTTON, "OPEN_ACCOUNT_BUTTON"),
        (ManagerLocators.CONSUMERS_BUTTON, "CONSUMERS_BUTTON"),
    ]

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, manager_page, button_locator, test_name):
        """
        Checking that all elements are visible
        :param driver: fixture
        :param manager_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
        """
        assert manager_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, manager_page, button_locator, test_name):
        """
        Checking that all elements are clickable
        :param driver: fixture
        :param manager_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        assert manager_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)
