import time


from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        url = self.browser.current_url
        assert url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', "URL is not presented "
        assert True

    def should_be_login_form(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        print("yes")
        assert True

    def should_be_register_form(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        print("yes")
        assert True

    def register_new_user(self, email, password):
        self.browser.get("http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        login_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        login_email.send_keys(email)
        login_pass = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        login_pass.send_keys(password)
        login_pass2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        login_pass2.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        login_button.click()
        time.sleep(1)
        assert self.is_element_present(*LoginPageLocators.REGISTER_USER_CORRECT), "Register  not is  successful"
        print("yes")
        assert True
