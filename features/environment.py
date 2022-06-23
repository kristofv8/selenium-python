from __future__ import unicode_literals

import os

from behave.log_capture import capture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@capture
def before_scenario(context, scenario):
    os.environ['GH_TOKEN'] = "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"
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://test.com/")
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()


@capture
def after_scenario(context, scenario):
    context.driver.quit()
