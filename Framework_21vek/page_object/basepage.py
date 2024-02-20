from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class BaseFunctions:
    def __init__(self, driver_chrome, url):
        self.driver_chrome = driver_chrome
        self.url = url

    def open(self):
        self.driver_chrome.get(self.url)

    def find_click_element(self, *locator):
        element = self.driver_chrome.find_element(*locator)
        element.click()
        return element

    def find_element(self, *locator):
        element = self.driver_chrome.find_element(*locator)
        return element

    def click_js(self, *locator, driver_chrome):
        element = self.driver_chrome.find_element(*locator)
        driver_chrome.execute_script("arguments[0].click();", element)

    def click_mouse(self, *locator, driver_chrome):
        element = self.driver_chrome.find_element(*locator)
        action = ActionChains(driver_chrome)
        action.move_to_element(element).click().perform()

    def move_mouse(self, *locator):
        element_to_hover_over = self.driver_chrome.find_element(*locator)
        actions = webdriver.ActionChains(self.driver_chrome)
        actions.move_to_element(element_to_hover_over).perform()

    def click_keyboard(self, *locator):
        element = self.driver_chrome.find_element(*locator)
        element.send_keys(Keys.ENTER)

    def send_keys(self, *locator, text):
        element = self.find_click_element(*locator)
        element.send_keys(text)
        return element

    def clear_text(self, *locator):
        element = self.find_click_element(*locator)
        element.clear()

    def alert_accept(self):
        alert = self.driver_chrome.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        alert = self.driver_chrome.switch_to.alert
        alert.dismiss()

    def prompt_alert(self, text):
        prompt = self.driver_chrome.switch_to.alert
        prompt.send_keys(text)
        prompt.accept()

    def new_window(self):
        self.driver_chrome.switch_to.window(self.driver_chrome.window_handles[-1])
