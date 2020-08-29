import time

import pytest

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