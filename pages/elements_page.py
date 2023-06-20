from locators.consumer_locators import ConsumerLocators
from locators.login_page_locators import LoginPageLocators
from locators.manager_locators import ManagerLocators
from locators.account_locators import AccountLocators
from locators.add_cust_locators import AddCustLocators
from locators.open_account_locators import OpenAccountLocators
from pages.base_page import BasePage
from data.deposit_withdraw_data import rand_withdraw, rand_deposit
from generator.person_generator import generated_person_data


class LoginPage(BasePage):
    locators = LoginPageLocators()


class ConsumerPage(BasePage):
    locators = ConsumerLocators()


class ManagerPage(BasePage):
    locators = ManagerLocators()


class AccountPage(BasePage):
    locators = AccountLocators()

    def fill_amount_deposit(self):
        random_deposit = rand_deposit()
        self.element_is_visible(self.locators.DEPOSIT_INPUT).send_keys(random_deposit)
        self.element_is_clickable(self.locators.DEPOSIT_SUBMIT_BUTTON).click()
        return random_deposit

    def fill_amount_withdraw(self):
        random_withdraw = rand_withdraw()
        self.element_is_visible(self.locators.WITHDRAW_INPUT).send_keys(random_withdraw)
        self.element_is_clickable(self.locators.WITHDRAW_SUBMIT_BUTTON).click()
        return random_withdraw


class AddCustPage(BasePage):
    locators = AddCustLocators()

    def fill_all_consumer_fields(self):
        first_name, last_name, post_code = generated_person_data()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.locators.POST_CODE_INPUT).send_keys(post_code)
        self.element_is_visible(self.locators.ADD_CONSUMER_BUTTON).click()


class OpenAccountPage(BasePage):
    locators = OpenAccountLocators()

