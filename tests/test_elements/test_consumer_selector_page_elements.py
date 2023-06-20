from selenium.webdriver.support.ui import Select
from locators.consumer_locators import ConsumerLocators
import pytest
from selenium.webdriver.common.by import By
from enums.errors_enums import ErrorMassages


class TestConsumerSelectorPageElements:

    buttons_locator_list = [
        (ConsumerLocators.HOME_BUTTON, "HOME_BUTTON"),
        (ConsumerLocators.CONSUMER_SELECT, "CONSUMER_SELECT"),
    ]

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, consumer_page, button_locator, test_name):
        """
        Checking that all elements are visible
        :param driver: fixture
        :param consumer_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
        """
        assert consumer_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)

    def test_login_button_is_not_visible(self, driver, consumer_page):
        """
        Checking that all LOGIN_BUTTON is not visible
        :param driver: fixture
        :param consumer_page: fixture
        :return: If the element is found, an error ELEMENT_IS_VISIBLE is returned
        """
        assert consumer_page.element_is_not_visible(ConsumerLocators.LOGIN_BUTTON), ErrorMassages.ELEMENT_IS_VISIBLE.value.format(ConsumerLocators.LOGIN_BUTTON)

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, consumer_page, button_locator, test_name):
        """
        Checking that all elements are clickable
        :param driver: fixture
        :param consumer_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        assert consumer_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)

    def test_dropdown_elements_are_clickable(self, driver, consumer_page):
        """
        Checking that all elements from dropdown are clickable
        :param driver: fixture
        :param consumer_page: fixture
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        select_element = consumer_page.element_is_present(ConsumerLocators.CONSUMER_SELECT)
        select = Select(select_element)
        options = select.options

        for option in options:
            assert consumer_page.element_is_clickable(option), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(option)

    def test_login_button_is_clickable(self, driver, consumer_page):
        """
        Checking that login button is clickable
        :param driver: fixture
        :param consumer_page: fixture
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        assert consumer_page.element_is_clickable(ConsumerLocators.CONSUMER_SELECT), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(ConsumerLocators.CONSUMER_SELECT)
        driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
        assert consumer_page.element_is_clickable(ConsumerLocators.CONSUMER_SELECT), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(ConsumerLocators.CONSUMER_SELECT)
        assert consumer_page.element_is_clickable(ConsumerLocators.LOGIN_BUTTON), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(ConsumerLocators.LOGIN_BUTTON)

