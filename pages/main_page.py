from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class MainPage(BasePage):

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_CARD)

    def is_ingredient_modal_visible(self):
        return self.find_element(MainPageLocators.INGREDIENT_HEADER).is_displayed()
    
    def click_close_modal(self):
        self.click_element(MainPageLocators.CLOSE_BUTTON)

    def is_modal_closed(self):
        return self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_HEADER))
    
    def get_ingredient_counter_value(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)
    
    def drag_and_drop_ingredient_to_order(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_CARD)
        basket = self.find_element(MainPageLocators.SECTION_BASKET)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, basket).perform()