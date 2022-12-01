from allure import title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('Registration')
def test_registration(setup):
    accept_cookie_settings()

    with step('Create account'):
        with step('Checking the display of the "Sign in or create an account" page"'):
            app.registration_user.checking_sign_in_page('Sign in or create an account')

            with step('Click button "Create your account"'):
                app.registration_user.click_create_account()

            with step('Email input page'):
                with step('Filling email address and click continue'):
                    app.registration_user.input_email('Enter your email address')

            with step('Password input page'):
                with step('Checking the display of the "create a password" page and input password'):
                    app.registration_user.input_password('Create a password')

                with step('Click button "Create account and sign in"'):
                    app.registration_user.click_create_account_and_sign_in()

    with step('Checking the display of the notification'):
        app.registration_user.checking_notification('Welcome to Booking.com!')

    with step('Start searching'):
        app.registration_user.start_searching()

    with step('Displaying the main page and the ability to search'):
        app.registration_user.checking_displaying_main_page('Enter your destination')
