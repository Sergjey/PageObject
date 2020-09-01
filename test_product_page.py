import time

import pytest

#from .pages.basket_page import BasketPage
#from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

#добавление товара в корзину со страницы товара
@pytest.mark.parametrize('numlink', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, numlink):
    #pytest.param(7, marks=pytest.mark.xfail)
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{numlink}"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_basket()
    page.solve_quiz_and_get_code()
    # вызываем один метод который наследует 4 других
    page.should_be_product_page()

#Проверяем, что нет сообщения об успехе с помощью is_not_element_present,
# падает сразу т.к. появляется сообщение об успешном добавлении
@pytest.mark.xfail(reason="This test should fall")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_product_message()

#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_product_message()

#Проверяем, что нет сообщения об успехе с помощью is_disappeared
@pytest.mark.xfail(reason="This test should fall")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappear_product_message()

#гость может перейти на страницу логина со страницы Х
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()