from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def login(self, email, password):
        email_field = self.find_element(LoginPageLocators.EMAIL_INPUT)
        email_field.send_keys()

        password_field = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        self.click_element(LoginPageLocators.LOGIN_BUTTON)
