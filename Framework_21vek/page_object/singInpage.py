import time
from page_object.basepage import BaseFunctions
from helpers.locators import Locators


class SignIn(BaseFunctions):

    def open_window_sing_in(self):
        self.find_click_element(*Locators.MAIN_USER)
        time.sleep(2)
        self.find_click_element(*Locators.MAIN_DropDown)
        time.sleep(2)

    def login(self, username: str, password: str):
        self.send_keys(*Locators.SING_IN_FILED, text=username)
        self.send_keys(*Locators.SING_IN_PASSWORD, text=password)

    def push_enter(self):
        self.find_click_element(*Locators.SING_IN_ENTER)

