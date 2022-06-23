from __future__ import unicode_literals

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RegisterPage:

    def __init__(self, context):
        self.driver = context.driver

    locators = {
        "name_input_field_create_account": (By.ID, 'id_register_name'),
        "email_address_input_field_create_account": (By.ID, "id_register_email"),
        "password_input_field_create_account": (By.ID, "id_register_password"),
        "create_an_account_confirm_button": (By.XPATH, '//span[contains(text(),"Create an account")]'),
        "accept_therms_of_service_checkbox": (By.CSS_SELECTOR, 'label[for="register-tos"]'),
        "invalid_email_message": (By.XPATH, '//li[contains(text(),"This value should be a valid email.")]'),
        "invalid_email_message_value_required": (By.CSS_SELECTOR, '#id_register_email+ul li'),
        "invalid_password_message": (By.CSS_SELECTOR, '#id_register_password+ul li'),
        "invalid_terms_of_service_message": (By.CSS_SELECTOR, '#parsley-id-multiple-register-tos>li'),
    }

    def fill_in_input_fields_create_account(self, email_create_account, password_create_account,
                                            name_create_account=""):
        email = self.driver.find_element(*self.locators["name_input_field_create_account"])
        email.send_keys(name_create_account)
        name = self.driver.find_element(*self.locators["email_address_input_field_create_account"])
        name.send_keys(email_create_account)
        password = self.driver.find_element(*self.locators["password_input_field_create_account"])
        password.send_keys(password_create_account)

    def click_create_an_account_confirm_button(self):
        confirm_button = self.driver.find_element(*self.locators["create_an_account_confirm_button"])
        confirm_button.click()

    def click_terms_of_service(self):
        terms_of_service = self.driver.find_element(*self.locators["accept_therms_of_service_checkbox"])
        terms_of_service.click()

    def check_error_message_email(self):
        error_message_email = self.driver.find_element(*self.locators["invalid_email_message"])
        return error_message_email.is_displayed()

    def check_error_message_email_value_required(self):
        error_message_value_required = self.driver.find_element(*self.locators["invalid_email_message_value_required"])
        return error_message_value_required.is_displayed()

    def check_error_message_password(self):
        error_message_password = self.driver.find_element(*self.locators["invalid_password_message"])
        return error_message_password.is_displayed()

    def check_error_message_terms_of_service(self):
        error_message_tos = self.driver.find_element(*self.locators["invalid_terms_of_service_message"])
        return error_message_tos.is_displayed()

    def clear_input_fields_create_account(self):
        clear_name_field = self.driver.find_element(*self.locators["name_input_field_create_account"])
        clear_name_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        clear_email_field = self.driver.find_element(*self.locators["email_address_input_field_create_account"])
        clear_email_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        clear_password_field = self.driver.find_element(*self.locators["password_input_field_create_account"])
        clear_password_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
