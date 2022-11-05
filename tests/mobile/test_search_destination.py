from allure import step, title, tag
from selene import have, be
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.model.authorization_booking import *
from diploma_project_tests.model.verify_booking import *


@tag('Browserstack mobile')
@title('Destination')
def test_search_destination(setup):
    accept_cookie_settings()
    authorization()
    verify_showing_welcome_message()

    with step('Search point of destination'):
        with step('Enter your destination'):
            browser.element((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_destination')).click()
        with step('Enter destination'):
            browser.element((AppiumBy.ID, 'com.booking:id/facet_with_bui_free_search_booking_header_toolbar_content')) \
                .type('Kyiv')

        with step('Destination options'):
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                             '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                             '1]/android.widget.TextView[1]')).should(have.text('Kyiv'))

        with step('Select from the list'):
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                             '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout '
                                             '/android.widget.LinearLayout/android.widget.FrameLayout/androidx'
                                             '.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')).click()

    with step('Adding date'):
        with step('Checking the calendar display'):
            browser.element((AppiumBy.ID, 'com.booking:id/calendar_week_days')).should(be.visible)

        with step('Date of arrival'):
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="09 November 2022"]')).click()

        with step('Сheck-out date'):
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="18 November 2022"]')).click()

        with step('Check the dates'):
            browser.element((AppiumBy.ID, 'com.booking:id/facet_date_picker_selection_summary')) \
                .should(have.text('Nov 9 - Nov 18 (9 nights)'))

        with step('Confirm the choice of dates'):
            browser.element((AppiumBy.ID, 'com.booking:id/facet_date_picker_confirm')).click()

    with step('The number of guests and rooms'):
        with step('Click and open block "Select rooms and guests"'):
            browser.element((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_occupancy')).click()

        with step('Displaying the block "Select rooms and guests"'):
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                             '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                                             '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.LinearLayout/android.widget.LinearLayout/android.widget.TextView'))\
                .should(have.text('Select rooms and guests'))

        with step('Change number of guests and rooms'):
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                             '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                                             '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup['
                                             '2]/android.widget.LinearLayout/android.widget.Button[1]')).click()
        with step('Apply changes'):
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                             '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                                             '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.LinearLayout/android.widget.RelativeLayout')).click()

    with step('Search for housing'):
        browser.element((AppiumBy.ID, 'com.booking:id/facet_search_box_cta')).click()

    with step('Checking the block title'):
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                         '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                                         '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                                         '.widget.TextView[1]')).should(have.text('Welcome to Booking.com!'))

    with step('Close welcome block'):
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                         '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                                         '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                                         '.widget.Button')).click()

    with step('Checking the results of a given search'):
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                         '/android.view.ViewGroup/android.widget.FrameLayout/android.widget'
                                         '.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx'
                                         '.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                         '1]/android.view.ViewGroup/android.widget.TextView[1]'))\
            .should(have.text('Visiting Ukraine'))
