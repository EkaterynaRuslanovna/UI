import allure
from allure_commons.types import AttachmentType
from locators.manager_locators import ManagerLocators
import pytest
from enums.errors_enums import ErrorMassages
from allure import severity_level


@allure.story('Scope of tests "manager page"')
class TestManagerPageElements:

    buttons_locator_list = [
        (ManagerLocators.HOME_BUTTON, "HOME_BUTTON"),
        (ManagerLocators.ADD_CONSUMER_BUTTON, "ADD_CONSUMER_BUTTON"),
        (ManagerLocators.OPEN_ACCOUNT_BUTTON, "OPEN_ACCOUNT_BUTTON"),
        (ManagerLocators.CONSUMERS_BUTTON, "CONSUMERS_BUTTON"),
    ]

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are visible')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_visible(self, driver, manager_page, button_locator, test_name):

        assert manager_page.element_is_visible(button_locator), ErrorMassages.ELEMENT_IS_NOT_VISIBLE.value.format(button_locator)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

    @allure.severity(severity_level.NORMAL)
    @allure.description('Checking that all elements are clickable')
    @pytest.mark.parametrize("button_locator, test_name", buttons_locator_list)
    def test_elements_are_clickable(self, driver, manager_page, button_locator, test_name):

        assert manager_page.element_is_clickable(button_locator), ErrorMassages.ELEMENT_IS_NOT_CLICKABLE.value.format(button_locator)
