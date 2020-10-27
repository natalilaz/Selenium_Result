from .pages.main_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest

class TestUserAddToBasketFromProductPage():
     @pytest.fixture(scope="function", autouse=True)
     def setup(self, browser):
         link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
         page = LoginPage(browser, link)
         page.open()
         page.go_to_login_page()
         email = str(time.time())+"@fakemail.org"
         password = "@#somefakepass19"
         page.register_new_user(email, password)
         page.should_be_authorized_user()

     def test_quest_cant_see_success_message(self, browser):
          self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
          page = ProductPage(browser, self.link)
          page.open()                          #открываем страницу товара
          page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
          
     def test_user_can_add_product_to_basket(self, browser):
          self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
          page = ProductPage(browser, self.link)
          page.open()
          page.add_product_to_basket() #добавление книги в корзину
          #page.solve_quiz_and_get_code() #рассчет кода 
          page.should_item_name_match() #сравнение название книги в корзине
          page.should_item_price_match() #сравнение цены книг в корзине
          
#def test_quest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket() #добавление книги в корзину
#     #page.solve_quiz_and_get_code() #рассчет кода 
#     page.should_item_name_match() #сравнение название книги в корзине
#     page.should_item_price_match() #сравнение цены книг в корзине

#def test_guest_should_see_login_link_on_product_page(browser):
#          link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#          page = ProductPage(browser, link)
#          page.open()
#          page.should_be_login_link()

#def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
          
     #@pytest.mark.xfail
     #def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
      #    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
      #    page = ProductPage(browser, link)
       #   page.open() #открываем страницу товара
        #  page.add_product_to_basket() #Добавляем товар в корзину
         # page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
     
     #@pytest.mark.xfail
     #def test_message_disappeared_after_adding_product_to_basket(browser):
      #    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
       #   page = ProductPage(browser, link)
        #  page.open() #открываем страницу товара
         # page.add_product_to_basket() #Добавляем товар в корзину
          #page.should_be_disappeared() #Проверяем, что нет сообщения об успехе с помощью is_disappeared
