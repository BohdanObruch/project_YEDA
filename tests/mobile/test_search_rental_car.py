from allure import title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('Search rental car')
def test_search_rental_car(setup):
    accept_cookie_settings()

    with step('Close authorization and registration page'):
        with step('Checking the display of sign in or create an account page'):
            app.rental_car.close_authorization_and_registration_page('Sign in or create an account')

    with step('Rewards & Wallet message'):
        app.rental_car.close_rewards_and_wallet_message('Rewards & Wallet')

    with step('Rental car page'):
        with step('Checking the availability of car rental tab'):
            app.rental_car.checking_the_availability_of_car_rental_tab('Car rental')

        with step('Open page and checking the display of the car rental page'):
            app.rental_car.open_page_rental_car('View and manage your car reservation')

        with step('Pickup location input'):
            app.rental_car.input_pickup_location_and_select_from_list('Kyiv')

        with step('Add date reservation'):
            app.rental_car.add_date_reservation('Nov 30 - Dec 9')

        with step('Add time reservation'):
            app.rental_car.add_time_reservation()

        with step('Search for cars in the specified dates and hours of reservation'):
            app.rental_car.search_car_in_the_specified_dates()

    with step('Page with search results'):
        with step('Checking the page with the results'):
            app.rental_car.checking_the_page_with_the_results('Visiting Ukraine')

        with step('Close banner'):
            app.rental_car.close_banner()

        with step('Switching to the first car card'):
            app.rental_car.switching_to_the_first_car_card()

            with step('Availability of a button for next booking'):
                app.rental_car.click_next_button_reservation_car('Next step', 'Booking Summary')

            with step('Next step booking'):
                app.rental_car.next_step_booking()

            with step('Main driver details page'):
                app.rental_car.checking_the_main_driver_details_page('Main driver details')
