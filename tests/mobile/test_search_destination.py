from allure import title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.model.authorization_booking import *
from diploma_project_tests.model.verify_booking import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('Destination')
def test_search_destination(setup):
    accept_cookie_settings()
    authorization()
    # verify_showing_welcome_message()

    with step('Search point of destination'):
        with step('Enter your destination'):
            app.search_destination.enter_destination('Kyiv')

        with step('Destination options'):
            app.search_destination.checking_the_availability_of_results('City in Ukraine')

        with step('Select from the list'):
            app.search_destination.select_from_list()

    with step('Adding date'):
        with step('Checking the calendar display'):
            app.search_destination.checking_the_calendar_display()

        with step('Add date of arrival'):
            app.search_destination.add_date_of_arrival()

        with step('Add date of departure'):
            app.search_destination.add_departure_date()

        with step('Confirm the choice of dates'):
            app.search_destination.confirm_the_choice_of_dates()

    with step('The number of guests and rooms'):
        with step('Click and open block "Select rooms and guests"'):
            app.search_destination.open_block_select_rooms_and_guests()

        with step('Displaying the block "Select rooms and guests"'):
            app.search_destination.check_block_select_rooms_and_guests('Select rooms and guests')

        with step('Change number of guests and rooms'):
            app.search_destination.change_number_of_guests_and_rooms()

        with step('Apply changes'):
            app.search_destination.apply_changes()

    with step('Search for housing'):
        app.search_destination.search_for_housing()

    # with step('Checking the block title'):
    #     app.search_destination.checking_the_block_title('Welcome to Booking.com!')
    #
    # with step('Close welcome block'):
    #     app.search_destination.close_welcome_block()

    with step('Checking the results of a given search'):
        app.search_destination.checking_the_results_of_a_given_search('Visiting Ukraine')
