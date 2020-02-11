import time

import pytest
from pytest import mark

from .pages import product_page
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page.click_add_product_to_basket(page)
    product_page.should_not_be_success_message(page)


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page.should_not_be_success_message(page)


@pytest.mark.xfail(strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page.click_add_product_to_basket(page)
    time.sleep(1)
    product_page.should_be_disappeared(page)
