from __future__ import unicode_literals

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmationPage:

    def __init__(self, context):
        self.driver = context.driver

    locators = {
        "iframe_confirmation_page": (By.ID, "mmContentReferrerStage1"),
        "iframe_page_close": (By.ID, "mmCloseButton")
    }

    def close_iframe_page(self):
        WebDriverWait(self.driver, 3).until(
            EC.frame_to_be_available_and_switch_to_it((self.locators["iframe_confirmation_page"])))
        iframe_close = self.driver.find_element(*self.locators["iframe_page_close"])
        iframe_close.click()
        self.driver.switch_to.default_content()
        self.driver.quit()
