import math

from selenium.common.exceptions import NoAlertPresentException
from pages.locators import GoodsPageLocators, ProductPageLocators


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
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")


def should_not_be_success_message(self):
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


def should_be_disappeared(self):
    assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Message is not disappeared, but should been disappeared"
