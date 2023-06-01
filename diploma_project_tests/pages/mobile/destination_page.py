from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared.jquery_style import s
import os

first_date = os.getenv('FIRST_DATE_BOOKING')
last_date = os.getenv('LAST_DATE_BOOKING')


class SearchDestinationPage:
    def enter_destination(self, value):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_destination')).click()
        s((AppiumBy.ID, 'com.booking:id/facet_with_bui_free_search_booking_header_toolbar_content')).type(value)
        return self

    def checking_the_availability_of_results(self, value):
        list_search_result = s((AppiumBy.ID, 'com.booking:id/facet_with_bui_free_search_booking_header_content'))
        list_search_result.element((AppiumBy.CLASS_NAME, 'android.view.ViewGroup'))\
            .element((AppiumBy.ID, 'com.booking:id/view_disambiguation_destination_subtitle')).should(have.text(value))
        return self

    def select_from_list(self):
        s((AppiumBy.ID, 'com.booking:id/view_disambiguation_destination_title')).click()
        return self

    def checking_the_calendar_display(self):
        s((AppiumBy.ID, 'com.booking:id/calendar_week_days')).should(be.visible)
        return self

    def add_date_of_arrival(self):
        s((AppiumBy.XPATH, f'{first_date}')).click()
        return self

    def add_departure_date(self):
        s((AppiumBy.XPATH, f'{last_date}')).click()
        return self

    def confirm_the_choice_of_dates(self):
        s((AppiumBy.ID, 'com.booking:id/facet_date_picker_confirm')).click()
        return self

    def open_block_select_rooms_and_guests(self):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_occupancy')).click()
        return self

    def check_block_select_rooms_and_guests(self, value):
        s((AppiumBy.XPATH, '//*[@text="Select rooms and guests"]')).should(have.text(value))
        return self

    def change_number_of_guests_and_rooms(self):
        adult_count = s((AppiumBy.ID, 'com.booking:id/group_config_adults_count'))
        adult_count.element((AppiumBy.ID, 'com.booking:id/bui_input_stepper_remove_button')).click()
        return self

    def apply_changes(self):
        s((AppiumBy.ID, 'com.booking:id/group_config_apply_button')).click()
        return self

    def search_for_housing(self):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_cta')).click()
        return self

    # def checking_the_block_title(self, value):
    #     s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
    #     return self
    #
    # def close_welcome_block(self):
    #     s((AppiumBy.ID, 'com.booking:id/bui_empty_state_primary_action')).click()
    #     return self

    def checking_the_results_of_a_given_search(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_banner_title')).should(have.text(value))
        return self
