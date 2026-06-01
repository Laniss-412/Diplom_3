from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)


    def get_text_from_element(self, locator):
        return self.find_element(locator).text
    
    def set_text_to_element(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)


    def wait_for_element_to_be_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    def drag_and_drop_elements(self, source, target):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def wait_for_urls(self, url):
        return self.wait.until(EC.url_to_be(url))
    
    def get_current_url(self):
        return self.driver.current_url
        
    def wait_for_valid_order_number(self, locator):
        return self.wait.until(
            lambda driver: (
                driver.find_element(*locator).text.strip().isdigit() and driver.find_element(*locator).text.strip() != "9999"))
    
    
    def wait_for_value_to_increase(self, locator, initial_value):
        return self.wait.until(lambda driver: int(driver.find_element(*locator).text.strip()) > int(initial_value))