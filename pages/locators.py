from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM_PASS_REP = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM_BUTTON = (By.CSS_SELECTOR,"button[name='registration_submit']")
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner:nth-child(2)")
       
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")

class BasketPageLocators():
    PRODUCT = (By.CSS_SELECTOR, "div.col-sm-4>h3>a")
    MESSAGE = (By.CSS_SELECTOR, "#content_inner>p>a")
    
