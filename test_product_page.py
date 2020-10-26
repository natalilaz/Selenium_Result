from .pages.main_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time
import pytest

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),                                  
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

#def test_guest_can_add_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket() #добавление книги в корзину
    #page.solve_quiz_and_get_code() #рассчет кода 
    #time.sleep(200)
    #page.should_item_name_match() #сравнение название книги в корзине
    #page.should_item_price_match() #сравнение цены книг в корзине
    #page.should_not_be_success_message()
    #page.should_be_disappeared()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     page = ProductPage(browser, link)
     page.open() #открываем страницу товара
     page.add_product_to_basket() #Добавляем товар в корзину
     page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
     
def test_guest_cant_see_success_message (browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     page = ProductPage(browser, link)
     page.open() #открываем страницу товара
     page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     page = ProductPage(browser, link)
     page.open() #открываем страницу товара
     page.add_product_to_basket() #Добавляем товар в корзину
     page.should_be_disappeared() #Проверяем, что нет сообщения об успехе с помощью is_disappeared
