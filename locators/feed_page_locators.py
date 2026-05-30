from selenium.webdriver.common.by import By

class FeedPageLocators:
    
    #Счетчик "Выполнено за все время"
    TOTAL_ORDERS_COUNTER = (By.XPATH, ".//div[./p[contains(text(), 'Выполнено за все время')]]//p[contains(@class, 'text_type_digits-large')]")

    #Счетчик "Выполнено за сегодня"
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//div[./p[contains(text(), 'Выполнено за сегодня')]]//p[contains(@class, 'text_type_digits-large')]")

    #Список номеров заказов в разделе "В работе"
    ORDERS_IN_WORK = (By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li") #Я не знаю почему, но классы перепутаны orderListReady путь к заказам "В работе", а не к готовым
    

