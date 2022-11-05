from allure import step, title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.pages.attractions_page import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('Search attractions')
def test_search_attractions(setup):
    accept_cookie_settings()

    with step('Close authorization and registration page'):
        with step('Checking the display of sign in or create an account page'):
            app.search_attractions.close_authorization_and_registration_page('Sign in or create an account')

    with step('Rewards & Wallet message'):
        app.search_attractions.close_rewards_and_wallet_message('Rewards & Wallet')

    with step('Scroll and go to the taxi page'):
        app.search_attractions.scroll_and_go_to_the_attractions_page('Attractions')

    with step('Attractions page'):
        with step('Checking the title of the search Attractions'):
            app.search_attractions.checking_the_title_of_the_search_attractions('Find and book a great experience')

        with step('Add locating'):
            app.search_attractions.add_locating('Kyiv')

        with step('Add date'):
            app.search_attractions.add_date()

        with step('Click Search Attractions'):
            app.search_attractions.search_attractions()
