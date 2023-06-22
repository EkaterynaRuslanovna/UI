import allure
from allure_commons.types import AttachmentType
from locators.add_cust_locators import AddCustLocators
import pytest
from enums.errors_enums import ErrorMassages
from allure import severity_level


@allure.story('Scope of tests "add customer page"')
class TestAddCustomerPageElements:

    buttons_locator_list = [
        (AddCustLocators.HOME_BUTTON, "HOME_BUTTON"),
        (AddCustLocators.FIRST_NAME_INPUT, "FIRST_NAME_INPUT"),
        (AddCustLocators.LAST_NAME_INPUT, "LAST_NAME_INPUT"),
        (AddCustLocators.POST_CODE_INPUT, "POST_CODE_INPUT"),
        (AddCustLocators.ADD_CONSUMER_BUTTON, "ADD_CONSUMER_BUTTON"),
    ]

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are visible')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, add_cust_page, button_locator, test_name):

        assert add_cust_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are clickable')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, add_cust_page, button_locator, test_name):

        assert add_cust_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)

    @allure.severity(severity_level.CRITICAL)
    @allure.description('Checking flow to fill all customer fields and add customer')
    def test_fill_all_fields(self, driver, add_cust_page):

        add_cust_page.fill_all_consumer_fields()
        assert "Customer added successfully with customer id :" in driver.switch_to.alert.text, ErrorMassages.FAILED_TO_ADD_CUSTOMER.value

