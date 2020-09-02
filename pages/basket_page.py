from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        basket_is_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert "Your basket is empty." in basket_is_empty_text, f"Basket is not empty"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "There are shouldn't be products in the basket"