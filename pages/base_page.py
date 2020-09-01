from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)#ожидание для выявления ошибок в is_element_present

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):#how как ищем BY ID, what что ищем id=link
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):#в скобках и в заголовке from selenium.common.exceptions \
            # указываемя имя_исключение, except (Exception) тогда будут ловиться ВСЕ исключения,\
            # а так только то что в скобках
            return False#implicity_wait будет возвращать True or False
        return True

    #проверяет, что элемент не появляется на странице в течение заданного времени
    #в product_page = should_not_be_product_message
    # is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    #Если же мы хотим проверить, что какой-то элемент исчезает,
    #то следует воспользоваться явным ожиданием вместе с функцией until_not,
    #в зависимости от того, какой результат мы ожидаем
    #is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    #Решение всплывающей задачи
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

        # для того, чтобы с любой страницы можно было перейти на страницу с логином, во избежание дублирования кода
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"