from allure import step, title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.model.authorization_booking import *
from diploma_project_tests.model.verify_booking import *
from diploma_project_tests.pages.favorite_list_page import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('adding_to_favorites_list')
def test_adding_to_favorites_list(setup):
    accept_cookie_settings()
    authorization()
    verify_showing_welcome_message()

    with step('Search point of destination'):
        with step('Enter your destination'):
            app.adding_to_favorite_list.search_point_of_destination('Kyiv')

        with step('Destination options'):
            app.adding_to_favorite_list.destination_options('Kyiv')

        with step('Select from the list'):
            app.adding_to_favorite_list.select_from_list()

    with step('Adding date'):
        with step('Checking the calendar display and add date arrival and check-out'):
            app.adding_to_favorite_list.adding_date('Nov 18 - Nov 27 (9 nights)')

    with step('The number of guests and rooms'):
        with step('Click and open block "Select rooms and guests"'):
            app.adding_to_favorite_list.the_number_of_guests_and_rooms('Select rooms and guests')

        with step('Change number of guests and rooms'):
            app.adding_to_favorite_list.change_number_of_guests_and_rooms()

    with step('Search for accommodation'):
        app.adding_to_favorite_list.search_for_accommodation()

    with step('Checking the welcome block'):
        app.adding_to_favorite_list.checking_the_welcome_block_title_and_close_him('Welcome to Booking.com!')

    with step('Scroll to another hotel'):
        app.adding_to_favorite_list.scroll_to_first_hotel()

    with step('Add first hotel to favorites'):
        app.adding_to_favorite_list.add_first_hotel_to_favorites('Saved to Kyiv')

    with step('Scroll to another hotel'):
        app.adding_to_favorite_list.scroll_to_second_hotel()

    with step('Add second hotel to favorites'):
        app.adding_to_favorite_list.add_second_hotel_to_favorites('Saved to Kyiv')
