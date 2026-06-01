from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def login(self, email, password):
        self.set_text_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.set_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
