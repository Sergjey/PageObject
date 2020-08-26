from selenium.common.exceptions import NoSuchElementException

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
        except (NoSuchElementException):#в скобках и в заголовке from selenium.common.exceptions указываемя имя_исключение
            return False#inplicity_wait будет возвращать True or False
        return True