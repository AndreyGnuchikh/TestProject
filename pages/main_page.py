import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, GoodsPageLocators
from .base_page import BasePage
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element_by_css_selector("#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def click_add_product_to_basket(self):
        assert self.is_element_present(*GoodsPageLocators.ADD_GOODS_IN_BASKET), "Basket button is not presented"
        add_button = self.browser.find_element(*GoodsPageLocators.ADD_GOODS_IN_BASKET)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.find_element_by_css_selector("#messages > div:nth-child(1) > div")
            print(f"Your code: {alert.text}")
            assert alert.text == "Coders at Work has been added to your basket."
        except NoAlertPresentException:
            print("No second alert presented")
