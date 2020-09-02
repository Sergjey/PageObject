from selenium.webdriver.common.by import By

#Класс главной страницы
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

#класс страницы с логином
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    #LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    REGISTER_FIELD_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FIELD_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FIELD_CONFIRM_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"][value=\"Register\"]")

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

# для того, чтобы с любой страницы можно было перейти на страницу с логином, во избежание дублирования кода
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default[href]")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")