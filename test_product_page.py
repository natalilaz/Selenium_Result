from .pages.main_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket() #добавление книги в корзину
    page.solve_quiz_and_get_code() #рассчет кода 
    #time.sleep(200)
    page.should_item_name_match() #сравнение название книги в корзине
    page.should_item_price_match() #сравнение цены книг в корзине
