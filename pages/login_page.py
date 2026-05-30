from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def login(self, email, password):
        email_field = self.find_element(LoginPageLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

        time.sleep(1)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        time.sleep(1)