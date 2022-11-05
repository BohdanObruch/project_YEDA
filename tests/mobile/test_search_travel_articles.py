from allure import step, title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.pages.articles_booking_page import *
from diploma_project_tests.helpers import app


@tag('Browserstack mobile')
@title('Search travel articles')
def test_search_travel_articles(setup):
    accept_cookie_settings()

    with step('Close authorization and registration page'):
        with step('Checking the display of sign in or create an account page'):
            app.search_articles.checking_sign_in_or_create_an_account_page('Sign in or create an account')

    with step('Rewards & Wallet message'):
        app.search_articles.close_rewards_and_wallet_message('Rewards & Wallet')

    with step('Search travel articles block'):
        with step('Scroll to travel articles block and open him'):
            app.search_articles.scroll_and_go_to_the_articles_page()

        with step('Checking the display on the page article'):
            app.search_articles.checking_the_display_on_the_article_page('Travel articles')

        with step('Manage cookie preferences'):
            app.search_articles.manage_cookie_preferences('Manage cookie preferences')

        with step('Checking the availability of the article and opening it'):
            app.search_articles.checking_the_availability_of_the_article_and_opening_it()
