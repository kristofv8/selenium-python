from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CheckoutPage:

    def __init__(self, context):
        self.driver = context.driver

    locators = {
        "first_name_input_field_delivery": (By.ID, "first_name"),
        "surname_delivery_input_field": (By.ID, "last_name"),
        "street_house_number_delivery_input_field": (By.ID, "street_address_1"),
        "postcode_delivery_input_field": (By.ID, "postal_code"),
        "city_delivery_input_field": (By.ID, "city"),
        "email_input_field_delivery_input_field": (By.ID, "email"),
        "phone_number_delivery_input_field": (By.ID, "tel"),
        "continue_to_payment_delivery": (By.XPATH, '//button[contains(text(), "Continue to payment")]')
    }

    def fill_in_first_name_checkout(self, first_name):
        first_name_delivery = self.driver.find_element(*self.locators["first_name_input_field_delivery"])
        first_name_delivery.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        first_name_delivery.send_keys(first_name)

    def fill_in_surname_checkout(self, last_name):
        surname_delivery = self.driver.find_element(*self.locators["surname_delivery_input_field"])
        surname_delivery.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        surname_delivery.send_keys(last_name)

    def fill_in_street_house_number_checkout(self, house_number):
        street_house_number_delivery = self.driver.find_element(
            *self.locators["street_house_number_delivery_input_field"])
        street_house_number_delivery.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        street_house_number_delivery.send_keys(house_number)

    def fill_in_postcode_checkout(self, postal_code):
        postcode_delivery = self.driver.find_element(*self.locators["postcode_delivery_input_field"])
        postcode_delivery.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        postcode_delivery.send_keys(postal_code)

    def fill_in_city_checkout(self, city):
        city_delivery = self.driver.find_element(*self.locators["city_delivery_input_field"])
        city_delivery.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        city_delivery.send_keys(city)

    def fill_in_email_checkout(self, email_checkout):
        email_input_field_delivery = self.driver.find_element(*self.locators["email_input_field_delivery_input_field"])
        email_input_field_delivery.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        email_input_field_delivery.send_keys(email_checkout)

    def fill_in_phone_number_checkout(self, phone_number_checkout):
        phone_number_delivery = self.driver.find_element(*self.locators["phone_number_delivery_input_field"])
        phone_number_delivery.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        phone_number_delivery.send_keys(phone_number_checkout)

    def click_continue_to_payment_checkout(self):
        continue_to_payment_delivery = self.driver.find_element(*self.locators["continue_to_payment_delivery"])
        continue_to_payment_delivery.click()
