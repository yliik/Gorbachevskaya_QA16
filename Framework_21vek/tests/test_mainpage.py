import time
import pytest
from helpers.locators import Locators
from page_object.mainpage import MainPage
from conftest import driver_chrome, handle_cookie


class TestMainPage:
    @pytest.mark.parametrize("locator_type, locator_value, url", [
        (*Locators.MAIN_CAT_ALL_OFFERS, "https://www.21vek.by/special_offers/promo.html"),
        (*Locators.MAIN_CAT_OFFERS,
         "https://www.21vek.by/special_offers/promo.html?discountTypes=sale"),
        (*Locators.MAIN_CAT_TIRES, "https://www.21vek.by/tires/"),
        (*Locators.MAIN_CAT_REFREG, "https://www.21vek.by/refrigerators/"),
        (*Locators.MAIN_CAT_MOBILE, "https://www.21vek.by/mobile/"),
        (*Locators.MAIN_CAT_NOTEBOOK, "https://www.21vek.by/notebooks/"),
        (*Locators.MAIN_CAT_TV, "https://www.21vek.by/tv/?filter%5B224869%5D%5Bfrom%5D=50"),
        (*Locators.MAIN_CAT_VACUUM, "(//*[@class='styles_promoItem__aolWq'])[8]"),
        (*Locators.MAIN_CAT_MATRAS, "https://www.21vek.by/mattresses/"),
        (*Locators.MAIN_CAT_SOFAS, "https://www.21vek.by/cushioned_furniture/"),
        (*Locators.MAIN_CAT_KITCHEN, "https://www.21vek.by/kitchen_furniture/"),
        (*Locators.MAIN_CAT_BATTERIES, "https://www.21vek.by/car_batteries/")
    ])
    def test_catalog(self, driver_chrome, locator_type, locator_value, url):
        catalog = MainPage(driver_chrome, "https://www.21vek.by")
        catalog.open()
        catalog.catalog(locator_type, locator_value)
        time.sleep(2)
        assert driver_chrome.current_url == url

    def test_discount_display(self, driver_chrome):
        discount_display = MainPage(driver_chrome, "https://www.21vek.by")
        discount_display.open()
        discount_display.find_click_element(*Locators.MAIN_GOODS_WITH_GIFTS)
        assert discount_display.find_element(*Locators.MAIN_ICON_GIFTS)

    def test_adding_in_cart(self, driver_chrome):
        adding_in_cart = MainPage(driver_chrome, "https://www.21vek.by")
        adding_in_cart.open()
        adding_in_cart.find_click_element(*Locators.MAIN_TO_BASKET)
        time.sleep(2)
        assert adding_in_cart.find_element(*Locators.MAIN_GOODS_IN_BASKET)

    def test_social_media_button(self, driver_chrome):
        social_media = MainPage(driver_chrome, "https://www.21vek.by")
        social_media.open()
        social_media.find_click_element(*Locators.MAIN_INSTAGRAM)
        social_media.new_window()
        assert driver_chrome.current_url == 'https://www.instagram.com/21vek.by/'
