from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared.jquery_style import s
import os
from dotenv import dotenv_values
from tests.conftest import dotenv

email_booking = dotenv.get('EMAIL_BOOKING')
password_booking = dotenv.get('PASSWORD_BOOKING')


def authorization():
    with step('Checking the display of the "Sign in or create an account" page"'):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text('Sign in or create an account'))

    with step('Sign in with email'):
        s((AppiumBy.ID, 'com.booking:id/identity_email_start')).click()

    with step('Email filling page'):
        with step('Filling email address'):
            s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text('Enter your email address'))
            s((AppiumBy.ID, 'com.booking:id/identity_text_input_edit_text')).type(email_booking)

        with step('Click button "Continue"'):
            s((AppiumBy.ID, 'com.booking:id/identity_email_continue')).click()

    with step('Password input page'):
        with step('Checking the display of the "Enter password" page'):
            s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text('Enter your password'))
        with step('Filling password'):
            s((AppiumBy.ID, 'com.booking:id/identity_text_input_edit_text')).type(password_booking)

        with step('Sign in'):
            s((AppiumBy.ID, 'com.booking:id/identity_password_continue')).click()
