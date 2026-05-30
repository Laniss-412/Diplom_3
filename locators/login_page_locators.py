from selenium.webdriver.common.by import By

class LoginPageLocators:
    #Поле ввода Email
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text' and @name='name']")

    #Поле ввода Пароль
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")

    #Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")