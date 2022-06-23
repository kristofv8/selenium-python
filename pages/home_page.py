from __future__ import unicode_literals

import time

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, context):
        self.driver = context.driver

    locators = {
        "thats_ok_button": (By.XPATH, '//button[contains(text(),"That’s OK")]'),
        "sign_in_button": (By.PARTIAL_LINK_TEXT, 'Sign in'),
        "products_menu_button": (By.CSS_SELECTOR, "label[for='megaMenuDesktop']"),
        "all_storage_solutions_link": (By.PARTIAL_LINK_TEXT, "All Storage Solutions")
    }

    def accept_cookie_bar(self):
        ok_button = self.driver.find_element(*self.locators["thats_ok_button"])
        ok_button.click()

    def click_sign_in_button(self):
        sign_in = self.driver.find_element(*self.locators["sign_in_button"])
        sign_in.click()

    def click_products_menu_button(self):
        products_button = self.driver.find_element(*self.locators["products_menu_button"])
        products_button.click()

    def click_all_storage_solutions(self):
        time.sleep(5)
        all_storage_solutions = self.driver.find_element(*self.locators["all_storage_solutions_link"])
        all_storage_solutions.click()
