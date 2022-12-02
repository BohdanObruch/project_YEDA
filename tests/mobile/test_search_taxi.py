from allure import title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('Search taxi')
def test_search_taxi(setup):
    accept_cookie_settings()

    with step('Close authorization and registration page'):
        with step('Checking the display of sign in or create an account page'):
            app.search_taxi.checking_sign_in_or_create_an_account_page('Sign in or create an account')

    with step('Rewards & Wallet message'):
        app.search_taxi.close_rewards_and_wallet_message('Rewards & Wallet')

    with step('Scroll and go to the taxi page'):
        app.search_taxi.scroll_and_go_to_the_taxi_page('Taxi')

    with step('Taxi page'):
        with step('Checking the title of the instructions'):
            app.search_taxi.checking_the_title_of_the_instructions('Trusted taxis around the world')

        with step('Skip instructions'):
            app.search_taxi.skip_instructions()

        with step('Book taxi for your trip page'):
            app.search_taxi.book_taxi()

            with step('Checking the title Route planner page'):
                app.search_taxi.checking_the_title_route_planner_page('Route planner')

            with step('Entering the initial location'):
                with step('Selecting a location from the list'):
                    app.search_taxi.input_start_location_and_select_from_the_list('Kyiv International Airport')

            with step('Entering the final location'):
                with step('Selecting a location from the list'):
                    app.search_taxi.input_final_location_and_select_from_the_list('DREAM Kyiv')

            with step('Select date and time'):
                app.search_taxi.select_date_and_time()

                with step('Change the default day'):
                    app.search_taxi.change_the_default_day()

        with step('Search taxi and view the results of the taxi order'):
            app.search_taxi.search_taxi("Visiting Ukraine")
