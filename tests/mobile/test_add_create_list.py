from allure import title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.model.authorization_booking import *
from diploma_project_tests.model.verify_booking import *
from diploma_project_tests.pages.mobile.favorite_list_page import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('Create_favorite_list')
def test_create_favorite_list(setup):
    accept_cookie_settings()
    authorization()
    verify_showing_welcome_message()

    with step('Create list favorite rooms and apartment'):
        with step('Checking the availability of the icon "Saved"'):
            app.create_list.checking_the_availability_of_the_icon('Saved')

        with step('Click on the icon "Saved"'):
            app.create_list.click_on_the_icon()

        with step('Checking the Saved page'):
            app.create_list.checking_the_saved_page('Keep what you like at hand')

        with step('Create a list'):
            with step('Adding title and submit'):
                app.create_list.create_list('Ukraine')

        with step('Checking the display of information on the Saved page'):
            app.create_list.checking_the_display_of_information('Ukraine', '0 properties')
