from __future__ import unicode_literals

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ShelfBookcasesPage:
    def __init__(self, context):
        self.driver = context.driver

    locators = {"checkout_button_product": (By.PARTIAL_LINK_TEXT, "Checkout"),
                "add_to_cart_button": (By.CLASS_NAME, 'cart-icon')
                }

    def open_shelf_bookases_page(self):
        self.driver.get("https://test.com/shelves")

    def click_add_to_cart_button(self):
        add_to_cart_button_available = WebDriverWait(self.driver, 5)
        add_to_cart_button = add_to_cart_button_available.until(
            EC.element_to_be_clickable(*self.locators["add_to_cart_button"]))
        add_to_cart_button.click()

    def click_checkout_button(self):
        checkout_button = self.driver.find_element(*self.locators["checkout_button_product"])
        checkout_button.click()
