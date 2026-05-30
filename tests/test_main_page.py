import pytest
import allure
from pages.main_page import MainPage
from urls import MAIN_PAGE_URLS
import time

@allure.feature("Конструктор на главной странице")
class TestMainPage:

    @allure.title("Проверка перехода по клику на кнопку 'Лента заказов'")
    def test_navigation_to_order_feed(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_URLS)
        time.sleep(3)
        
        main_page.click_order_feed()

        assert "/feed" in driver.current_url


    @allure.title("Проверка открытия окна с деталями при клике на ингредиент")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_URLS)
        time.sleep(3)

        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_visible() is True


    @allure.title("Проверка закрытия окна с деталями ингредиента при клике на крестик")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_URLS)
        time.sleep(3)
        
        main_page.click_ingredient()
        main_page.click_close_modal()

        assert main_page.is_modal_closed()


    @allure.title("Проверка увеличения счетчика при добавлении ингредиента в заказ")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_URLS)

        initial_counter = int(main_page.get_ingredient_counter_value())
        main_page.drag_and_drop_ingredient_to_order()
        time.sleep(2)
        new_counter = int(main_page.get_ingredient_counter_value())

        assert new_counter > initial_counter