from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage #осуществляет переход на страниц с логином

class MainPage(BasePage):
    # переход к странице логина
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url) #осуществляет переход на логин страницу

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login_link is not presented"