from selenium.webdriver import ActionChains
from conftest import driver_chrome
from page_object.basepage import BaseFunctions
from selenium import webdriver


class MainPage(BaseFunctions):

    def catalog(self, locator_type, locator_value):
        self.find_click_element(locator_type, locator_value)
