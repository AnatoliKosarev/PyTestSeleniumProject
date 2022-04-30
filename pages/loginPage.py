from .basePage import BasePage
from .locators import LoginPageLocators
from utils.error_messages import get_missing_element_error_message


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login/' in self.browser.current_url, 'URL does not contain "/login/"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), get_missing_element_error_message('Login form')

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), get_missing_element_error_message(
            'Register form')
