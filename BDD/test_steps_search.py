import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@given("the user is on the 21vek.by homepage")
def open_homepage(driver_chrome):
    pass


@when(parsers.parse('the user searches for "{search_term}"'))
def search_for_product(driver_chrome, search_term):
    search_box = driver_chrome.find_element(By.ID, "catalogSearch")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)


@then("the search results page is displayed")
def verify_search_results_page(driver_chrome):
    assert driver_chrome.find_element(By.XPATH, "(//*[@class='b-recipes__item__link j-category__link'])[1]")