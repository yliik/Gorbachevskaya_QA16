from page_object.singInpage import SignIn
from helpers.locators import Locators
from conftest import driver_chrome
from conftest import handle_cookie


class TestSingIn:
    def test_login_password(self, driver_chrome):
        sing_in = SignIn(driver_chrome, "https://www.21vek.by")
        sing_in.open()
        sing_in.open_window_sing_in()
        sing_in.login("juli.01071369@gmail.com", "nupKub-5rovge-ruswyh")
        sing_in.push_enter()
        assert driver_chrome.find_element(*Locators.MAIN_USER_ICON)

    def test_negative_login_password(self, driver_chrome):
        sing_in = SignIn(driver_chrome, "https://www.21vek.by")
        sing_in.open()
        sing_in.open_window_sing_in()
        sing_in.login("juli@gmail.com", "nup11111111")
        sing_in.push_enter()
        assert driver_chrome.find_element(*Locators.SING_IN_ERROR)
