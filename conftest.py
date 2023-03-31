import pytest
from selenium import webdriver
from pages.registration_page import Registration
from pages.authorization_page import Authorization


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def auth(browser):
    auth = Authorization(browser)
    return auth


@pytest.fixture(scope="session")
def registr(browser):
    registr = Registration(browser)
    return registr
