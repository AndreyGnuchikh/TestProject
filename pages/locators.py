from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class GoodsPageLocators:
    ADD_GOODS_IN_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    BASKET_CLICK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs "
                                     "> span > a")
    BASKET_EMPTY = (By.CSS_SELECTOR, "# content_inner > div.row > div:nth-child(1) > div.sub-header > h2")
    BASKET_EMPTY_MASSAGE = (By.CSS_SELECTOR, "#content_inner > p")
