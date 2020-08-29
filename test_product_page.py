from .pages.product_page import ProductPage
import time

#добавление товара в корзину со страницы товара
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_page() #вызываем один метод который наследует 4 других
    time.sleep(3)