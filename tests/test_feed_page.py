import pytest
import allure
import time
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from urls import FEED_PAGE_URLS, MAIN_PAGE_URLS

@allure.feature("Страница 'Лента заказов'")
class TestFeedPage:

    @allure.title("Проверка увеличения счетчика 'Выполнено за все время' при оформлении заказа")
    def test_total_orders_counter_increases(self, login_user):
        main_page = MainPage(login_user)
        feed_page = FeedPage(login_user)

        login_user.get(FEED_PAGE_URLS)
        time.sleep(3)
        initial_total = int(feed_page.get_total_orders_value())

        login_user.get(MAIN_PAGE_URLS)
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_make_order_button()
        time.sleep(4)
        main_page.click_close_modal()

        login_user.get(FEED_PAGE_URLS)
        time.sleep(3)
        new_total = int(feed_page.get_total_orders_value())

        assert new_total > initial_total


    @allure.title("Проверка увеличения счетчика 'Выполнено за сегодня' при оформлении заказа")
    def test_today_orders_counter_increases(self, login_user):
        main_page = MainPage(login_user)
        feed_page = FeedPage(login_user)

        login_user.get(FEED_PAGE_URLS)
        time.sleep(2)
        initial_today = int(feed_page.get_today_orders_value())

        login_user.get(MAIN_PAGE_URLS)
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_make_order_button()
        time.sleep(4)
        main_page.click_close_modal()

        login_user.get(FEED_PAGE_URLS)
        time.sleep(2)
        new_today = int(feed_page.get_today_orders_value())

        assert new_today > initial_today


    @allure.title("Проверка появления нового заказа в разделе 'В работе'")
    def test_new_order_in_work_board(self, login_user):
        main_page = MainPage(login_user)
        feed_page = FeedPage(login_user)

        login_user.get(MAIN_PAGE_URLS)
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_make_order_button()
        time.sleep(4)

        order_number = main_page.get_created_order_number()
        main_page.click_close_modal()

        login_user.get(FEED_PAGE_URLS)
        time.sleep(7)
        work_orders = feed_page.get_orders_in_work_list()

        assert f"0{order_number}" in work_orders
        