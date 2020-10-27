from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL некорректный - без логина"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" 
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASS)
        password_field.send_keys(password)
        rep_password_field= self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASS_REP)
        rep_password_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_BUTTON)
        assert button, "No found"
        button.click()
