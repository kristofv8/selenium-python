from __future__ import unicode_literals

from behave import given, when, then

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@when(
    "User fills in input fields with invalid email value, valid password, accept Terms Of Service and clicks Create An Account button")
def fill_in_input_fields_invalid_email(context):
    register_page = RegisterPage(context)
    register_page.clear_input_fields_create_account()
    register_page.fill_in_input_fields_create_account("joemailinator.com",
                                                      "123Joetylko456"
                                                      , "")
    register_page.click_terms_of_service()
    register_page.click_create_an_account_confirm_button()


@given("User clicks Sign in and after that Create An Account Button")
def open_create_account_functionality(context):
    home_page = HomePage(context)
    home_page.accept_cookie_bar()
    home_page.click_sign_in_button()
    login_page = LoginPage(context)
    login_page.click_create_account_page()


@then("User sees a message about invalid email")
def see_invalid_email_message(context):
    register_page = RegisterPage(context)
    assert register_page.check_error_message_email()


@when(
    "User fills in input field with valid email value, doesnt fill in password, accept Terms Of Service and clicks Create An Account button")
def fill_in_input_fields_invalid_password(context):
    register_page = RegisterPage(context)
    register_page.clear_input_fields_create_account()
    register_page.fill_in_input_fields_create_account("spacestar@mailinator.com", "", "")
    register_page.click_terms_of_service()
    register_page.click_create_an_account_confirm_button()


@then("User sees message that password  value is required")
def see_invalid_password_message(context):
    register_page = RegisterPage(context)
    assert register_page.check_error_message_password()


@when(
    "User fills in input fields with valid email value, valid password, doesnt accept Terms Of Service and clicks Create An Account button")
def dont_accept_terms_of_service(context):
    register_page = RegisterPage(context)
    register_page.clear_input_fields_create_account()
    register_page.fill_in_input_fields_create_account("spacestar@mailinator.com", "123Joetylko456", "")
    register_page.click_create_an_account_confirm_button()


@then("User sees message that accept Terms Of Service is required")
def see_tos_is_required_message(context):
    register_page = RegisterPage(context)
    assert register_page.check_error_message_terms_of_service()


@when("User doesnt fill in email, password, doesnt accept Terms Of Service")
def fill_in_input_fields_invalid_email_password_dont_accept_tos(context):
    register_page = RegisterPage(context)
    register_page.clear_input_fields_create_account()
    register_page.fill_in_input_fields_create_account("", "", "")
    register_page.click_create_an_account_confirm_button()


@then("User sees that all values are required")
def see_all_values_are_required_message(context):
    register_page = RegisterPage(context)
    assert register_page.check_error_message_email_value_required()
    assert register_page.check_error_message_password()
    assert register_page.check_error_message_terms_of_service()
