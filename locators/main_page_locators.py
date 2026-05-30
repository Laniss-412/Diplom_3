from selenium.webdriver.common.by import By

class MainPageLocators:

    #Кнопка "Конструктор" в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']") 
    
    #Кнопка "Лента заказов" в шапке
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    
    #Первый ингридиент со страницы "Флюорисцентеная булка R2-D3"
    INGREDIENT_CARD = (By.XPATH, "//a[.//p[text()='Флюоресцентная булка R2-D3']]")
    
    #Заголовок всплывающего окна "Детали ингредиента"
    INGREDIENT_HEADER = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    
    #Кнопка для закрытия всплывающего окна "Детали ингредиента"
    CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    
    #Счетчик на карточке ингридиента
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    
    #Область куда нужно перетаскивать ингредиент
    SECTION_BASKET = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    
    #Кнопка "Оформить заказ"
    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    #Текст с номером заказа
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title')]")