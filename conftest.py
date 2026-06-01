import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login_page import LoginPage
from urls import LOGIN_PAGE_URLS, MAIN_PAGE_URLS


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        
    driver.set_window_size(1920, 1080)
    
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver):
    login_page = LoginPage(driver)
    driver.get(LOGIN_PAGE_URLS)
    login_page.login("tester_12_12_12@yandex.ru", "123456")
    login_page.wait_for_urls(MAIN_PAGE_URLS)
    return driver