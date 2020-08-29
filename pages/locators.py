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
    #товар и добавление товара
    ITEM = (By.CSS_SELECTOR, ".item.active")
    ADD_ITEM = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    #цена на странице и в корзине + название товара на странице и в сообщении
    PRICE_ON_PAGES_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs:nth-child(2)")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-safe.alert-noicon.alert-success:nth-child(1) strong")