import pytest
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from urls import FEED_PAGE_URLS, MAIN_PAGE_URLS

@allure.feature("Страница 'Лента заказов'")
class TestFeedPage:

    @allure.title("Проверка увеличения счетчика 'Выполнено за все время' при оформлении заказа")
    def test_total_orders_counter_increases(self, login_user):
        main_page = MainPage(login_user)
        feed_page = FeedPage(login_user)

        with allure.step("Переход на страницу ленты заказов и получение начального счетчика"):
            login_user.get(FEED_PAGE_URLS)
            feed_page.wait_for_urls(FEED_PAGE_URLS)
            initial_total = int(feed_page.get_total_orders_value())

        with allure.step("Переход на главную страницу и оформление заказа"):
            login_user.get(MAIN_PAGE_URLS)
            main_page.wait_for_urls(MAIN_PAGE_URLS)
            main_page.drag_and_drop_ingredient_to_order()
            main_page.click_make_order_button()
            main_page.click_close_modal()

        with allure.step("Возврат в ленту заказов и проверка увелечения счетчика"):
            login_user.get(FEED_PAGE_URLS)
            feed_page.wait_for_urls(FEED_PAGE_URLS)
            feed_page.wait_for_total_counter_to_increase(initial_total)
            new_total = int(feed_page.get_total_orders_value())

        assert new_total > initial_total


    @allure.title("Проверка увеличения счетчика 'Выполнено за сегодня' при оформлении заказа")
    def test_today_orders_counter_increases(self, login_user):
        main_page = MainPage(login_user)
        feed_page = FeedPage(login_user)

        with allure.step("Переход на страницу ленты заказов и получение начального счетчика за сегодня"):
            login_user.get(FEED_PAGE_URLS)
            feed_page.wait_for_urls(FEED_PAGE_URLS)
            initial_today = int(feed_page.get_today_orders_value())

        with allure.step("Переход на главную страницу и оформление заказа"):
            login_user.get(MAIN_PAGE_URLS)
            main_page.wait_for_urls(MAIN_PAGE_URLS)
            main_page.drag_and_drop_ingredient_to_order()
            main_page.click_make_order_button()
            main_page.click_close_modal()

        with allure.step("Возврат в ленту заказов и проверка увеличения счетчика за сегодня"):
            login_user.get(FEED_PAGE_URLS)
            feed_page.wait_for_urls(FEED_PAGE_URLS)
            feed_page.wait_for_today_counter_to_increase(initial_today)
            new_today = int(feed_page.get_today_orders_value())

        assert new_today > initial_today


    @allure.title("Проверка появления нового заказа в разделе 'В работе'")
    def test_new_order_in_work_board(self, login_user):
        main_page = MainPage(login_user)
        feed_page = FeedPage(login_user)

        with allure.step("Переход на главную страницу и оформление заказа"):
            login_user.get(MAIN_PAGE_URLS)
            main_page.wait_for_urls(MAIN_PAGE_URLS)
            main_page.drag_and_drop_ingredient_to_order()
            main_page.click_make_order_button()

        with allure.step("Получение номера созданного заказа и закрытие модального окна"):
            order_number = main_page.get_created_order_number()
            main_page.click_close_modal()

        with allure.step("Переход в ленту заказов и получение списка заказов 'В работе'"):
            login_user.get(FEED_PAGE_URLS)
            feed_page.wait_for_urls(FEED_PAGE_URLS)
            work_orders = feed_page.get_orders_in_work_list()

        assert f"0{order_number}" in work_orders
        