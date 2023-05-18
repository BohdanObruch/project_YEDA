from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared.jquery_style import s
from diploma_project_tests.command import swipe_helper
from tests.conftest import dotenv

first_date = dotenv.get('FIRST_DATE_BOOKING')
last_date = dotenv.get('LAST_DATE_BOOKING')


class CreateListPage:
    def checking_the_availability_of_the_icon(self, value):
        s((AppiumBy.XPATH, '//*[@text="Saved"]')).with_(timeout=3).should(have.text(value))
        return self

    def click_on_the_icon(self):
        s((AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Saved"]')).click()
        return self

    def checking_the_saved_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/tv_wishlist_empty_title')).should(have.text(value))
        return self

    def create_list(self, value):
        s((AppiumBy.ID, 'com.booking:id/btn_wishlist_empty_create_list')).click()
        s((AppiumBy.ID, 'com.booking:id/wishlist_create_edit_text')).type(value)
        s((AppiumBy.ID, 'com.booking:id/btn_wishlist_create_list')).click()
        return self

    def checking_the_display_of_information(self, value_one: str, value_two: str):
        s((AppiumBy.ID, 'com.booking:id/tv_wishlist_name')).should(have.text(value_one))
        s((AppiumBy.ID, 'com.booking:id/tv_wishlist_property')).should(have.text(value_two))
        return self


class AddingToFavoriteListPage:
    def search_point_of_destination(self, value):
        s((AppiumBy.ID, 'facet_search_box_accommodation_destination')).click()
        s((AppiumBy.ID, 'facet_with_bui_free_search_booking_header_toolbar_content')).type(value)
        return self

    def destination_options(self, value):
        list_search_result = s((AppiumBy.ID, 'facet_with_bui_free_search_booking_header_content'))
        list_search_result.element((AppiumBy.CLASS_NAME, 'android.view.ViewGroup'))\
            .element((AppiumBy.ID, 'com.booking:id/view_disambiguation_destination_subtitle')).should(have.text(value))
        return self

    def select_from_list(self):
        s((AppiumBy.ID, 'com.booking:id/view_disambiguation_destination_title')).click()
        return self

    def adding_date(self):
        s((AppiumBy.ID, 'com.booking:id/calendar_week_days')).should(be.visible)
        s((AppiumBy.XPATH, f'{first_date}')).click()
        s((AppiumBy.XPATH, f'{last_date}')).click()
        s((AppiumBy.ID, 'com.booking:id/facet_date_picker_confirm')).with_(timeout=3).click()
        return self

    def the_number_of_guests_and_rooms(self, value):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_occupancy')).with_(timeout=3).click()
        s((AppiumBy.XPATH, '//*[@text="Select rooms and guests"]')).should(have.text(value))
        return self

    def change_number_of_guests_and_rooms(self):
        adult_count = s((AppiumBy.ID, 'com.booking:id/group_config_adults_count'))
        adult_count.element((AppiumBy.ID, 'com.booking:id/bui_input_stepper_remove_button')).click()
        s((AppiumBy.ID, 'com.booking:id/group_config_apply_button')).click()
        return self

    def search_for_accommodation(self):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_cta')).click()
        return self

    # def checking_the_welcome_block_title_and_close_him(self, value):
    #     s((AppiumBy.XPATH, '//*[@text="Welcome to Booking.com!"]')).should(have.text(value))
    #
    #     s((AppiumBy.XPATH, '//android.view.ViewGroup/android.widget.Button')).click()
    #     return self

    def scroll_to_first_hotel(self):
        swipe_helper.swipe_to_down_one_block()
        return self

    def add_first_hotel_to_favorites(self, value):
        s((AppiumBy.XPATH, '//android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup['
                           '2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')).click()
        s((AppiumBy.ID, 'com.booking:id/snackbar_text')).should(have.text(value))
        return self

    def scroll_to_second_hotel(self):
        swipe_helper.swipe_to_down_one_block()
        return self

    def add_second_hotel_to_favorites(self, value):
        s((AppiumBy.XPATH, '//android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup['
                           '2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')).click()
        s((AppiumBy.ID, 'com.booking:id/snackbar_text')).should(have.text(value))
        return self


class DeletingFromFavoriteListPage:
    def go_to_saved_tab(self):
        s((AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Saved"]')).click()
        return self

    def check_the_number_of_houses_added(self, value):
        s((AppiumBy.ID, 'com.booking:id/tv_wishlist_property')).should(have.text(value))
        return self

    def open_favorites_list(self):
        s((AppiumBy.ID, 'com.booking:id/tv_wishlist_name')).click()
        return self

    def uncheck_the_box_you_like_house(self):
        s((AppiumBy.ID, 'com.booking:id/sr_property_card_wishlist')).click()
        return self

    def checking_what_is_displayed_in_the_favorites_list(self, value):
        s((AppiumBy.ID, 'com.booking:id/wishlist_properties_number')).with_(timeout=5).should(have.text(value))
        return self

    def checking_that_the_deletion_message_is_displayed(self, value):
        s((AppiumBy.ID, 'com.booking:id/snackbar_action')).should(have.text(value))
        return self
