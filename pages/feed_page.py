from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

class FeedPage(BasePage):

    def get_total_orders_value(self):
        return self.get_text_from_element(FeedPageLocators.TOTAL_ORDERS_COUNTER)

    def get_today_orders_value(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_ORDERS_COUNTER)

    def wait_for_today_counter_to_increase(self, initial_today):
        self.wait_for_value_to_increase(FeedPageLocators.TODAY_ORDERS_COUNTER, initial_today)

    def wait_for_total_counter_to_increase(self, initial_total):
        self.wait_for_value_to_increase(FeedPageLocators.TOTAL_ORDERS_COUNTER, initial_total)

    def get_orders_in_work_list(self):
        self.wait.until(lambda driver: driver.find_elements(*FeedPageLocators.ORDERS_IN_WORK) and driver.find_elements(*FeedPageLocators.ORDERS_IN_WORK)[0].text.strip() != "Все текущие заказы готовы!")
        
        elements = self.find_elements(FeedPageLocators.ORDERS_IN_WORK)
        numbers_list = []
        for el in elements:
            numbers_list.append(el.text)
            
        return numbers_list