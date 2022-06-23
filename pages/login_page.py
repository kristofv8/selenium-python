from __future__ import unicode_literals

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, context):
        self.driver = context.driver

    locators = {
        "email_input_field_loging": (By.ID, "id_login_username"),
        "password_input_field_loging": (By.ID, "id_login_password"),
        "login_button_loging": (By.ID, "login_submit_button"),
        "create_an_account_button": (By.XPATH, "//span[text()='Create an account']")
    }

    def login_as_user(self, email, password):
        email_field = self.driver.find_element(*self.locators["email_input_field_loging"])
        email_field.send_keys(email)
        password_field = self.driver.find_element(*self.locators["password_input_field_loging"])
        password_field.send_keys(password)
        login_button = self.driver.find_element(*self.locators["login_button_loging"])
        login_button.click()

    def click_create_account_page(self):
        create_account_button = self.driver.find_element(*self.locators["create_an_account_button"])
        create_account_button.click()
