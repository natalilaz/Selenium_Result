from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner:nth-child(2)")
       
