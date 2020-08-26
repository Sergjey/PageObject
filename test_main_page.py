from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.go_to_login_page() #выполняем метод страницы - открываем страницу логина
    #browser.get(link)
    #login_link = browser.find_element_by_css_selector("#login_link")
    #login_link.click()