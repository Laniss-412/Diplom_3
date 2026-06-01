from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver import ActionChains

class MainPage(BasePage):

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_CARD)

    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_HEADER)
    
    def click_close_modal(self):
        self.click_element(MainPageLocators.CLOSE_BUTTON)

    def is_modal_closed(self):
        return self.wait_for_element_to_be_invisible(MainPageLocators.INGREDIENT_HEADER)
    
    def get_ingredient_counter_value(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)
    
    def drag_and_drop_ingredient_to_order(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_CARD)
        basket = self.find_element(MainPageLocators.SECTION_BASKET)
        
        if "firefox" in self.driver.name.lower():
            js_script = """
            var source = arguments[0];
            var target = arguments[1];
            
            function createEvent(type) {
                var event = document.createEvent('CustomEvent');
                event.initCustomEvent(type, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(type, val) { this.data[type] = val; },
                    getData: function(type) { return this.data[type]; }
                };
                return event;
            }
            
            function dispatch(element, type, event) {
                if (element.dispatchEvent) { element.dispatchEvent(event); }
            }
            
            var dragStartEvent = createEvent('dragstart');
            dispatch(source, 'dragstart', dragStartEvent);
            
            var dragOverEvent = createEvent('dragover');
            dragOverEvent.dataTransfer = dragStartEvent.dataTransfer;
            dispatch(target, 'dragover', dragOverEvent);
            
            var dropEvent = createEvent('drop');
            dropEvent.dataTransfer = dragStartEvent.dataTransfer;
            dispatch(target, 'drop', dropEvent);
            
            var dragEndEvent = createEvent('dragend');
            dragEndEvent.dataTransfer = dragStartEvent.dataTransfer;
            dispatch(source, 'dragend', dragEndEvent);
            """
            self.execute_script(js_script, ingredient, basket)
        else:
            self.drag_and_drop_elements(ingredient, basket)
            
    
    def click_make_order_button(self):
        self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    def get_created_order_number(self):
        self.wait_for_valid_order_number(MainPageLocators.ORDER_NUMBER)
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
    