from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_USER_CORRECT = (By.CSS_SELECTOR, "#messages > div > div")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    BUTTON_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    ADD_GOODS_IN_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_CLICK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs "
                                     "> span > a")
    BASKET_EMPTY = (By.CSS_SELECTOR, "# content_inner > div.row > div:nth-child(1) > div.sub-header > h2")
    BASKET_EMPTY_MASSAGE = (By.CSS_SELECTOR, "#content_inner > p")
