import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from locators.consumer_locators import ConsumerLocators
from pages.elements_page import LoginPage, ConsumerPage, ManagerPage, AccountPage, AddCustPage, OpenAccountPage
from locators.manager_locators import ManagerLocators


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    page.open()
    return page


@pytest.fixture()
def consumer_page(driver):
    page = ConsumerPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
    page.open()
    return page


@pytest.fixture()
def manager_page(driver):
    page = ManagerPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')
    page.open()
    return page


@pytest.fixture(scope="module")
def account_page(driver):
    page = AccountPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer')
    page.open()
    page.element_is_clickable(ConsumerLocators.CONSUMER_SELECT).click()
    driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
    driver.find_element(By.ID, "userSelect").click()
    dropdown = driver.find_element(By.ID, "userSelect")
    dropdown.find_element(By.XPATH, "//option[. = 'Hermoine Granger']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    element = driver.find_element(By.CSS_SELECTOR, ".btn-default")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    return page


@pytest.fixture()
def add_cust_page(driver):
    page = AddCustPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')
    page.open()
    time.sleep(1)
    driver.find_element(*ManagerLocators.ADD_CONSUMER_BUTTON).click()
    return page


@pytest.fixture()
def open_account_page(driver):
    page = OpenAccountPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')
    page.open()
    time.sleep(1)
    driver.find_element(*ManagerLocators.OPEN_ACCOUNT_BUTTON).click()
    return page
