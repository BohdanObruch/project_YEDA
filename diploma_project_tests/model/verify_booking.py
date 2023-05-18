from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from allure import step
from selene.support.shared.jquery_style import s


def verify_showing_welcome_message():
    with step('Checking the display of the notification'):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text('Welcome to Booking.com!'))

    with step('Start searching'):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_primary_action')).click()


def verify_search_capability():
    with step('Displaying the main page and the ability to search'):
        input_destination = s((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_destination'))\
            .with_(timeout=5).should(be.visible)
        input_destination.element((AppiumBy.ID, 'com.booking:id/facet_search_box_basic_field_label'))\
            .should(have.text('Enter your destination'))
