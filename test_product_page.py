import time

import pytest

from pages import product_page
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage



def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket_page()
    page.should_be_basket_text()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.email = str(time.time()) + "@fakemail.org"
        self.password = "npTN3urMP8fMx7M"
        self.link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.page = LoginPage(browser, self.link)
        self.page.register_new_user(self.email, self.password)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page.should_not_be_success_message(page)

    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo"
                                      "=newYear2019",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      pytest.param(
                                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                          marks=pytest.mark.xfail),
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        product_page.click_add_product_to_basket(page)
        product_page.solve_quiz_and_get_code(page)
        alert = page.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        print(f"Your code: {alert.text}")
        assert alert.text == "Coders at Work has been added to your basket."
