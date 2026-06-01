import pytest
import allure
from pages.main_page import MainPage
from urls import MAIN_PAGE_URLS


@allure.feature("Конструктор на главной странице")
class TestMainPage:

    @allure.title("Проверка перехода по клику на кнопку 'Лента заказов'")
    def test_navigation_to_order_feed(self, driver):
        main_page = MainPage(driver)

        with allure.step("Переход на главную страницу"):
            driver.get(MAIN_PAGE_URLS)
            main_page.wait_for_urls(MAIN_PAGE_URLS)
        
        with allure.step("Клик по кнопке 'Лента заказов'"):
            main_page.click_order_feed()

        main_page.wait_for_urls(f"{MAIN_PAGE_URLS}feed")
        assert "/feed" in main_page.get_current_url()


    @allure.title("Проверка открытия окна с деталями при клике на ингредиент")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Переход на главную страницу"):
            driver.get(MAIN_PAGE_URLS)
            main_page.wait_for_urls(MAIN_PAGE_URLS)

        with allure.step("Клик по карточке ингредиента"):
            main_page.click_ingredient()

        assert main_page.is_ingredient_modal_visible() is True


    @allure.title("Проверка закрытия окна с деталями ингредиента при клике на крестик")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Переход на главную страницу и открытие модального окна"):
            driver.get(MAIN_PAGE_URLS)
            main_page.wait_for_urls(MAIN_PAGE_URLS)
            main_page.click_ingredient()
        
        with allure.step("Клик по кнопке закрытия(крестик) модального окна"):
            main_page.click_close_modal()

        assert main_page.is_modal_closed()


    @allure.title("Проверка увеличения счетчика при добавлении ингредиента в заказ")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Переход на главную страницу и получение начального значения счетчика"):
            driver.get(MAIN_PAGE_URLS)
            main_page.wait_for_urls(MAIN_PAGE_URLS)
            initial_counter = int(main_page.get_ingredient_counter_value())

        with allure.step("Перетаскивание ингредиента в корзину"):
            main_page.drag_and_drop_ingredient_to_order()
        
        with allure.step("Получение нового значения счетчика"):
            new_counter = int(main_page.get_ingredient_counter_value())

        assert new_counter > initial_counter