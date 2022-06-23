from __future__ import unicode_literals

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class PaymentMethodsPage:

    def __init__(self, context):
        self.driver = context.driver

    locators = {
        "mastercard_payment_option": (By.XPATH, '//*[@id="credit_card_form"]/div[2]/div[4]/div/div'),
        "submit_button_mastercard": (By.CSS_SELECTOR, '[type="submit"]'),
        "card_number_payment_methods": (By.ID, "card.cardNumber"),
        "card_holder_payments_methods": (By.ID, "card.cardHolderName"),
        "card_expiry_month_payment_methods": (By.ID, "card.expiryMonth"),
        "card_expiry_year_payment_methods": (By.ID, "card.expiryYear"),
        "cvc_payment_methods": (By.ID, "card.cvcCode"),
        "continue_button_payment": (By.CSS_SELECTOR, "input[value='continue']"),
        "pay_button_payment": (By.ID, "mainSubmit")
    }

    def choose_payment_method(self):
        mastercard_option = self.driver.find_element(
            *self.locators["mastercard_payment_option"])
        mastercard_option.click()
        submit_button_available = WebDriverWait(self.driver, 3)
        mastercard_pay_button = submit_button_available.until(
            EC.element_to_be_clickable(self.locators["submit_button_mastercard"]))
        mastercard_pay_button.click()

    def fill_in_payment_details(self, card_number, card_owner, card_expiry_month, card_expiry_year, card_cvc):
        card_number_payment = self.driver.find_element(*self.locators["card_number_payment_methods"])
        card_number_payment.send_keys(card_number)
        card_holder_payment = self.driver.find_element(*self.locators["card_holder_payments_methods"])
        card_holder_payment.send_keys(card_owner)
        card_expiry_month_payment = Select(
            self.driver.find_element(*self.locators["card_expiry_month_payment_methods"]))
        card_expiry_month_payment.select_by_value(card_expiry_month)
        card_expiry_year_payment = Select(self.driver.find_element(*self.locators["card_expiry_year_payment_methods"]))
        card_expiry_year_payment.select_by_value(card_expiry_year)
        cvc_payment = self.driver.find_element(*self.locators["cvc_payment_methods"])
        cvc_payment.send_keys(card_cvc)

    def click_continue_button_payment(self):
        continue_button = self.driver.find_element(*self.locators["continue_button_payment"])
        continue_button.click()

    def click_payment_button(self):
        pay_button = self.driver.find_element(*self.locators["pay_button_payment"])
        pay_button.click()
