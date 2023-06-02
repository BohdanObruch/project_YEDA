from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared.jquery_style import s
from diploma_project_tests.command import swipe_helper
import os


first_date = os.getenv('FIRST_DATE_BOOKING')
last_date = os.getenv('LAST_DATE_BOOKING')


class RentalCarPage:

    def close_authorization_and_registration_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        return self

    def close_rewards_and_wallet_message(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
        swipe_helper.swipe_to_close_wallet_message()
        return self

    def checking_the_availability_of_car_rental_tab(self, value):
        s((AppiumBy.XPATH, '//*[@text="Car rental"]')).should(have.text(value))
        return self

    def open_page_rental_car(self, value):
        s((AppiumBy.XPATH, '//*[@text="Car rental"]')).click()
        s((AppiumBy.ID, 'com.booking:id/banner_description')).should(have.text(value))
        return self

    def input_pickup_location_and_select_from_list(self, value):
        s((AppiumBy.ID, 'com.booking:id/search_box_edit_pick_up_location')).click()
        s((AppiumBy.ID, 'com.booking:id/search_query_edittext')).type(value)
        s((AppiumBy.ID, 'com.booking:id/ape_rc_view_location_name')).click()
        return self

    def add_date_reservation(self):
        s((AppiumBy.ID, 'com.booking:id/bgoc_search_box_date_pick_up')).click()
        s((AppiumBy.XPATH, f'{first_date}')).click()
        s((AppiumBy.XPATH, f'{last_date}')).click()
        s((AppiumBy.ID, 'com.booking:id/calendar_confirm')).click()
        return self

    def add_time_reservation(self):
        s((AppiumBy.ID, 'com.booking:id/search_box_time_pick_up')).click()
        s((AppiumBy.XPATH, '//*[contains(@text,"12:00")]')).click()
        return self

    def search_car_in_the_specified_dates(self):
        s((AppiumBy.ID, 'com.booking:id/search_box_btn_search')).click()
        return self

    def checking_the_page_with_the_results(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_banner_title')).should(have.text(value))
        return self

    def close_banner(self):
        s((AppiumBy.ID, 'com.booking:id/bui_banner_close_button')).click()
        return self

    def switching_to_the_first_car_card(self):
        s((AppiumBy.ID, 'com.booking:id/or_similar')).click()
        return self

    def click_next_button_reservation_car(self, button_next: str, summary_page: str):
        s((AppiumBy.XPATH, '//*[@text="Next step"]')).should(have.text(button_next)).click()
        s((AppiumBy.XPATH, '//*[@text="Booking Summary"]')).should(have.text(summary_page))
        return self

    def next_step_booking(self):
        s((AppiumBy.XPATH, '//*[@text="Next step"]')).click()
        return self

    def checking_the_main_driver_details_page(self, value):
        s((AppiumBy.XPATH, '//*[@text="Main driver details"]')).should(have.text(value))
        return self
