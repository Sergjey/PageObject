from selenium.webdriver.common.by import By

#Класс главной страницы
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

#класс страницы с логином
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")

#класс со страницей продукта
class ProductPageLocators():
    ITEM = (By.CSS_SELECTOR, ".item.active")
    ADD_ITEM = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    CHOOSEN_ITEM = (By.CSS_SELECTOR, ".alertinner")