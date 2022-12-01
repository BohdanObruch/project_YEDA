import os

from allure import step
from dotenv import load_dotenv
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


email_booking = os.getenv('EMAIL_BOOKING')
password_booking = os.getenv('PASSWORD_BOOKING')


def authorization():
    with step('Checking the display of the "Sign in or create an account" page"'):
        browser.element((AppiumBy.ID, 'com.booking:id/identity_header_title')) \
            .should(have.text('Sign in or create an account'))

    with step('Sign in with email'):
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout['
                                         '2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                         '.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android'
                                         '.widget.LinearLayout/android.widget.FrameLayout['
                                         '1]/android.widget.FrameLayout/android.widget.Button')).click()

    with step('Email filling page'):
        with step('Filling email address'):
            browser.element((AppiumBy.ID, 'com.booking:id/identity_header_title')) \
                .should(have.text('Enter your email address'))
            browser.element((AppiumBy.ID, 'com.booking:id/identity_text_input_edit_text')).type(email_booking)

        with step('Click button "Continue"'):
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                                             '.FrameLayout['
                                             '2]/android.widget.LinearLayout/android.widget.FrameLayout/android'
                                             '.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.FrameLayout/android.widget.Button')).click()

    with step('Password input page'):
        with step('Checking the display of the "Enter password" page'):
            browser.element((AppiumBy.ID, 'com.booking:id/identity_header_title')) \
                .should(have.text('Enter your password'))
        with step('Filling password'):
            browser.element((AppiumBy.ID, 'com.booking:id/identity_text_input_edit_text')).type(password_booking)

        with step('Sign in'):
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                                             '.FrameLayout['
                                             '2]/android.widget.LinearLayout/android.widget.FrameLayout/android'
                                             '.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout['
                                             '1]/android.widget.FrameLayout/android.widget.Button')).click()
