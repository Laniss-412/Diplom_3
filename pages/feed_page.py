from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

class FeedPage(BasePage):

    def get_total_orders_value(self):
        return self.get_text_from_element(FeedPageLocators.TOTAL_ORDERS_COUNTER)
    

    def get_today_orders_value(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_ORDERS_COUNTER)
    
    def get_orders_in_work_list(self):
        self.find_element(FeedPageLocators.ORDERS_IN_WORK)
        elements = self.driver.find_elements(*FeedPageLocators.ORDERS_IN_WORK)
        clean_number_list = []

        for el in elements:
            clean_text = el.text.replace("0\n", "")
            clean_number_list.append(clean_text)

        return clean_number_list