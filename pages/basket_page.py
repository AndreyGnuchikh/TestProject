from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_CLICK)
        link.click()

    def should_be_empty_basket_page(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is empty"

    def should_be_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MASSAGE), "Basket text is presented"
