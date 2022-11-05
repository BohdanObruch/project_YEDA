from allure import step, title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.model.authorization_booking import *
from diploma_project_tests.model.verify_booking import *
from diploma_project_tests.pages.favorite_list_page import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('Deleting_houses_from_the_favorites_list')
def test_deleting_houses_from_the_favorites_list(setup):
    accept_cookie_settings()
    authorization()
    verify_showing_welcome_message()

    with step('Deleting houses from the favorites list'):
        with step('Go to the "Saved" tab'):
            app.deleting_from_favorite_list.go_to_saved_tab()

        with step('Check the number of houses added'):
            app.deleting_from_favorite_list.check_the_number_of_houses_added('2 properties')

        with step('Open favorites list'):
            app.deleting_from_favorite_list.open_favorites_list()

        with step('Uncheck the box you like'):
            app.deleting_from_favorite_list.uncheck_the_box_you_like_house()

        with step('Checking what is displayed minus one house in the favorites list'):
            app.deleting_from_favorite_list.checking_what_is_displayed_in_the_favorites_list('1 property  Show on map')

        with step('Checking that the deletion message is displayed'):
            app.deleting_from_favorite_list.checking_that_the_deletion_message_is_displayed('UNDO')
