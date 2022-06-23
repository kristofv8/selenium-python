from __future__ import unicode_literals

from behave import given, then

from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.payment_methods_page import PaymentMethodsPage
from pages.shelf_bookcases_page import ShelfBookcasesPage


@given('User logs in to his account "{email}", "{password}"')
def open_page_log_to_account(context, email, password):
    home_page = HomePage(context)
    home_page.accept_cookie_bar()
    home_page.click_sign_in_button()
    login_page = LoginPage(context)
    login_page.login_as_user(email, password)


@then("Clicks Products in main menu and choose All Storage Solutions")
def click_products_all_storage_solutions_buttons(context):
    home_page = HomePage(context)
    home_page.click_products_menu_button()
    home_page.click_all_storage_solutions()


@then(
    "Goes to Products Page selects second Bookcase and clicks Add To Cart and Checkout buttons")
def choose_bookcase_click_add_to_cart_checkout_buttons(context):
    shelf_bookcases_page = ShelfBookcasesPage(context)
    shelf_bookcases_page.open_shelf_bookases_page()
    shelf_bookcases_page.click_add_to_cart_button()
    shelf_bookcases_page.click_checkout_button()


@then(
    'User fills in Delivery Form with his credentials, "{first_name}", "{last_name}", "{house_number}", "{postal_code}", "{city}", "{email_checkout}", "{phone_number_checkout}" etc. and clicks Continue To Payment button')
def fill_in_delivery_details(context, first_name, last_name, house_number, postal_code, city, email_checkout,
                             phone_number_checkout):
    checkout_page = CheckoutPage(context)
    checkout_page.fill_in_first_name_checkout(first_name)
    checkout_page.fill_in_surname_checkout(last_name)
    checkout_page.fill_in_street_house_number_checkout(house_number)
    checkout_page.fill_in_postcode_checkout(postal_code)
    checkout_page.fill_in_city_checkout(city)
    checkout_page.fill_in_email_checkout(email_checkout)
    checkout_page.fill_in_phone_number_checkout(phone_number_checkout)
    checkout_page.click_continue_to_payment_checkout()


@then(
    'Choose payment method, fills in payment details "{card_number}", "{card_owner}", "{card_expiry_month}", "{card_expiry_year}", "{card_cvc}" and clicks Continue and after that Payment button')
def complete_payment(context, card_number, card_owner, card_expiry_month, card_expiry_year, card_cvc):
    payment_methods_page = PaymentMethodsPage(context)
    payment_methods_page.choose_payment_method()
    payment_methods_page.fill_in_payment_details(card_number, card_owner, card_expiry_month, card_expiry_year, card_cvc)
    payment_methods_page.click_continue_button_payment()
    payment_methods_page.click_payment_button()


@then(
    "User is able to see discount information close it, and goes to Confirmation Page")
def close_iframe_see_confirmation_page(context):
    confirmation_page = ConfirmationPage(context)
    confirmation_page.close_iframe_page()
