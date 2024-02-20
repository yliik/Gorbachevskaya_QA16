import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given, when, then
from selenium.webdriver.common.by import By


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@given("the user is on the 21vek.by homepage")
def open_homepage(driver_chrome):
    driver_chrome.get("https://www.21vek.by")


@when("the user navigates to the shop page from the menu")
def navigate_to_shop(driver_chrome):
    xpath = '//*[@id="header"]/div/div[4]/div/div/ul/li[3]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()


@then("the shop page is displayed")
def verify_shop_page(driver_chrome):
    assert driver_chrome.title == 'Купить холодильник в Минске, холодильники в рассрочку - 21vek.by'
    assert driver_chrome.current_url == 'https://www.21vek.by/refrigerators/'