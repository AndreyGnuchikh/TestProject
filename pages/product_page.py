import math

from selenium.common.exceptions import NoAlertPresentException

from pages.locators import GoodsPageLocators


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