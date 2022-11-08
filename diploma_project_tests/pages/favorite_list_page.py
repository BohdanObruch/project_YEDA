import time
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


class CreateList:
    def checking_the_availability_of_the_icon(self, value):
        s((AppiumBy.XPATH, '//android.widget.FrameLayout['
                           '@content-desc="Saved"]/android.widget.FrameLayout/android.widget.TextView'
                           '')).should(have.text(value))
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


class AddingToFavoriteList:
    def search_point_of_destination(self, value):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_destination')).click()
        s((AppiumBy.ID, 'com.booking:id/facet_with_bui_free_search_booking_header_toolbar_content')) \
            .type(value)
        return self

    def destination_options(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                           '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                           '1]/android.widget.TextView[1]')).should(have.text(value))
        return self

    def select_from_list(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout '
                           '/android.widget.LinearLayout/android.widget.FrameLayout/androidx'
                           '.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')).click()
        return self

    def adding_date(self, value):
        s((AppiumBy.ID, 'com.booking:id/calendar_week_days')).should(be.visible)
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="18 November 2022"]')).click()
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="27 November 2022"]')).click()
        s((AppiumBy.ID, 'com.booking:id/facet_date_picker_selection_summary')).should(have.text(value))
        time.sleep(1)
        s((AppiumBy.ID, 'com.booking:id/facet_date_picker_confirm')).click()
        time.sleep(1)
        return self

    def the_number_of_guests_and_rooms(self, value):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_occupancy')).click()
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget'
                           '.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                           '.TextView')) \
            .should(have.text(value))
        return self

    def change_number_of_guests_and_rooms(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup['
                           '2]/android.widget.LinearLayout/android.widget.Button[1]')).click()
        s((AppiumBy.ID, 'com.booking:id/group_config_apply_button')).click()
        return self

    def search_for_accommodation(self):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_cta')).click()
        return self

    def checking_the_welcome_block_title_and_close_him(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.TextView[1]')).should(have.text(value))

        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.Button')).click()
        return self

    def scroll_to_first_hotel(self):
        browser.driver.swipe(470, 1400, 470, 600, 330)
        return self

    def add_first_hotel_to_favorites(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                           '/android.view.ViewGroup/android.widget.FrameLayout/android.widget'
                           '.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx'
                           '.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                           '4]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup['
                           '1]/android.view.ViewGroup/android.widget.ImageView')).click()
        s((AppiumBy.ID, 'com.booking:id/snackbar_text')).should(have.text(value))
        return self

    def scroll_to_second_hotel(self):
        browser.driver.swipe(470, 1400, 470, 200, 330)
        return self

    def add_second_hotel_to_favorites(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view'
                           '.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup'
                           '/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view'
                           '.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup['
                           '1]/android.view.ViewGroup/android.widget.ImageView')).click()

        s((AppiumBy.ID, 'com.booking:id/snackbar_text')).should(have.text(value))
        return self


class DeletingFromFavoriteList:
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
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout['
                           '2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx'
                           '.recyclerview.widget.RecyclerView/android.widget.FrameLayout['
                           '1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout'
                           '/android.view.ViewGroup[1]/android.widget.ImageView')).click()
        return self

    def checking_what_is_displayed_in_the_favorites_list(self, value):
        time.sleep(2)
        s((AppiumBy.ID, 'com.booking:id/wishlist_properties_number')).should(have.text(value))
        return self

    def checking_that_the_deletion_message_is_displayed(self, value):
        s((AppiumBy.ID, 'com.booking:id/snackbar_action')).should(have.text(value))
        return self
