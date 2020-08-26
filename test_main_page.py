from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time

#тесты для MainPage
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    time.sleep(5)
    page.go_to_login_page() #выполняем метод страницы - открываем страницу логина
    login_page = page.go_to_login_page()#осуществляем переход на страницу с логином
    login_page.should_be_login_page()
    time.sleep(5)

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    #time.sleep(5)
    page.should_be_login_link()

#тесты для LoginPage
def test_guest_should_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    #time.sleep(5)
    page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    #time.sleep(5)
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    #time.sleep(5)
    page.should_be_register_form()