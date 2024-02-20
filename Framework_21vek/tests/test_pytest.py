import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from conftest import driver_chrome
from conftest import handle_cookie
from helpers.locators import Locators


@pytest.mark.parametrize("locator_type, locator_value, url", [
        (*Locators.MAIN_CAT_ALL_OFFERS, "https://www.21vek.by/special_offers/promo.html"),
        (*Locators.MAIN_CAT_OFFERS,
         "https://www.21vek.by/special_offers/promo.html?discountTypes=sale"),
        (*Locators.MAIN_CAT_TIRES, "https://www.21vek.by/tires/"),
        (*Locators.MAIN_CAT_REFREG, "https://www.21vek.by/refrigerators/"),
        (*Locators.MAIN_CAT_MOBILE, "https://www.21vek.by/mobile/"),
        (*Locators.MAIN_CAT_NOTEBOOK, "https://www.21vek.by/notebooks/"),
        (*Locators.MAIN_CAT_TV, "https://www.21vek.by/tv/?filter%5B224869%5D%5Bfrom%5D=50"),
        (*Locators.MAIN_CAT_VACUUM, "https://www.21vek.by/vacuum/"),
        (*Locators.MAIN_CAT_MATRAS, "https://www.21vek.by/mattresses/"),
        (*Locators.MAIN_CAT_SOFAS, "https://www.21vek.by/cushioned_furniture/"),
        (*Locators.MAIN_CAT_KITCHEN, "https://www.21vek.by/kitchen_furniture/"),
        (*Locators.MAIN_CAT_BATTERIES, "https://www.21vek.by/car_batteries/")
    ])
def test_catalog(driver_chrome, locator_type, locator_value, url):
    catalog_link = driver_chrome.find_element(locator_type, locator_value)
    catalog_link.click()
    time.sleep(2)
    assert driver_chrome.current_url == url


@pytest.mark.discount_display
def test_discount_display(driver_chrome):
    xpath = "//*[text()='Товары с подарками']"
    element = driver_chrome.find_element(By.XPATH,xpath)
    element.click()
    assert driver_chrome.find_element(By.XPATH, '//*[text()="+ Подарок"]')


@pytest.mark.mobile_version
def test_display_button_mobile(driver_chrome):
    driver_chrome.set_window_size(828,1792)
    driver_chrome.refresh()
    exampl_button = driver_chrome.find_element(By.XPATH, "(//*[@class='Banners_sideBanner__bsw_S'])[1]")
    assert exampl_button.is_displayed()


@pytest.mark.filters
def test_discount_display_filter_price(driver_chrome):
    xpath = "//*[@class='SpecialOffersList_link__fOWwb']"
    element_button = driver_chrome.find_element(By.XPATH, xpath)
    element_button.click()
    time.sleep(5)
    price_button = driver_chrome.find_element(By.XPATH, "(//*[@class='NewInput_inputStyle__2uziF'])[2]")
    price_button.send_keys("50")
    price_button.send_keys(Keys.RETURN)
    time.sleep(2)
    price = driver_chrome.find_element(By.XPATH, "(//*[@class='style_currentPrice__Lp9e2' and text()='25,90 р.'])[1]")
    price_text = price.text.strip()
    price_value = float(price_text.replace(" р.", "").replace(",", "."))
    assert price_value <= 50


@pytest.mark.filters
@pytest.mark.xfail
def test_filter_negative(driver_chrome):
    xpath = "(//*[@class='Chip_label__oZTDw ChipHome_label__pG1wI'])[7]"
    element_button = driver_chrome.find_element(By.XPATH, xpath)
    element_button.click()
    time.sleep(2)
    price = driver_chrome.find_element(By.XPATH, "(//*[@data-testid='card-current-price' and text()='85,80 р.'])[2]")
    price_text = price.text.strip()
    price_value = float(price_text.replace(" р.", "").replace(",", "."))
    assert price_value >= 100