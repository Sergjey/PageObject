from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not a registration page address"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FIELD_EMAIL)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTER_FIELD_PASS)
        pass_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_FIELD_CONFIRM_PASS)
        email_field.send_keys(email)
        pass_field.send_keys(password)
        pass_confirm_field.send_keys(password)
        register_submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        register_submit_button.click()