from locators.add_cust_locators import AddCustLocators
import pytest
from enums.errors_enums import ErrorMassages


class TestAddCustomerPageElements:

    buttons_locator_list = [
        (AddCustLocators.HOME_BUTTON, "HOME_BUTTON"),
        (AddCustLocators.FIRST_NAME_INPUT, "FIRST_NAME_INPUT"),
        (AddCustLocators.LAST_NAME_INPUT, "LAST_NAME_INPUT"),
        (AddCustLocators.POST_CODE_INPUT, "POST_CODE_INPUT"),
        (AddCustLocators.ADD_CONSUMER_BUTTON, "ADD_CONSUMER_BUTTON"),
    ]

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, add_cust_page, button_locator, test_name):
        """
        Checking that all elements are visible
        :param driver: fixture
        :param add_cust_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not found, an error ELEMENT_IS_NOT_VISIBLE is returned
        """
        assert add_cust_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)

    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, add_cust_page, button_locator, test_name):
        """
        Checking that all elements are clickable
        :param driver: fixture
        :param add_cust_page: fixture
        :param button_locator: locator from buttons_locator_list
        :param test_name: test name
        :return: If the element is not clickable, an error ELEMENT_IS_NOT_CLICKABLE is returned
        """
        assert add_cust_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)

    def test_fill_all_fields(self, driver, add_cust_page):
        """
        Checking flow to fill all customer fields and add customer
        :param driver: fixture
        :param add_cust_page: fixture
        :return: If the customer did not add, an error FAILED_TO_ADD_CUSTOMER is returned
        """
        add_cust_page.fill_all_consumer_fields()
        assert "Customer added successfully with customer id :" in driver.switch_to.alert.text, ErrorMassages.FAILED_TO_ADD_CUSTOMER.value
