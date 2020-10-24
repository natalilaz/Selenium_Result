from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        assert button, "No found"
        button.click()
    def should_item_name_match(self):
        name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        print(name)
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        print(added_name)
        assert name == added_name, "Error text"


    def should_item_price_match(self):
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        print(price)
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text
        print(added_price)
        assert price == added_price, "Error price"
        
