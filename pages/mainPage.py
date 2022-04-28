from selenium.webdriver.common.by import By

from .basePage import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.ID, 'login_link')
        login_link.click()
