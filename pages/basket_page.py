from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
       "Product is presented, but should not be"

    def should_be_message_abot_emty(self):
        assert not(self.is_not_element_present(*BasketPageLocators.MESSAGE)), \
       "Message is not presented, but should be"
