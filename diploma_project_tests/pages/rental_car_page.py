import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


class RentalCar:

    def close_authorization_and_registration_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        return self

    def close_rewards_and_wallet_message(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
        browser.driver.swipe(720, 683, 720, 2070, 400)
        return self

    def checking_the_availability_of_car_rental_tab(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                           '2]/android.widget.FrameLayout['
                           '1]/android.widget.LinearLayout/androidx.recyclerview.widget'
                           '.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView')) \
            .should(have.text(value))
        return self

    def open_page_rental_car(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                           '2]/android.widget.FrameLayout['
                           '1]/android.widget.LinearLayout/androidx.recyclerview.widget'
                           '.RecyclerView/android.widget.LinearLayout[3]')).click()

        s((AppiumBy.ID, 'com.booking:id/banner_description')).should(have.text(value))
        return self

    def input_pickup_location_and_select_from_list(self, value):
        s((AppiumBy.ID, 'com.booking:id/search_box_edit_pick_up_location')).click()
        s((AppiumBy.ID, 'com.booking:id/search_query_edittext')).type(value)
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                           '.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                           '1]/android.widget.LinearLayout')).click()

        return self

    def add_date_reservation(self, value):
        s((AppiumBy.ID, 'com.booking:id/bgoc_search_box_date_pick_up')).click()
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="30 November 2022"]')).click()
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="09 December 2022"]')).click()
        s((AppiumBy.ID, 'com.booking:id/selected_dates')).should(have.text(value))
        s((AppiumBy.ID, 'com.booking:id/calendar_confirm')).click()
        return self

    def add_time_reservation(self):
        s((AppiumBy.ID, 'com.booking:id/search_box_time_pick_up')).click()
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.LinearLayout/android.widget.FrameLayout/android.widget.ListView'
                           '/android.widget.CheckedTextView[9]')).click()
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
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android'
                           '.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android'
                           '.view.ViewGroup['
                           '1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')).click()
        return self

    def click_next_button_reservation_car(self, button_next: str, summary_page: str):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/androidx.compose.ui'
                           '.platform.ComposeView/android.view.View/android.view.View/android'
                           '.view.View[3]/android.widget.TextView')) \
            .should(have.text(button_next)).click()

        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.view'
                           '.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout'
                           '/android.widget.TextView')).should(have.text(summary_page))
        return self

    def next_step_booking(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.view'
                           '.ViewGroup/android.widget.LinearLayout/android.widget.Button')).click()
        return self

    def checking_the_main_driver_details_page(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView'
                           '/android.widget.LinearLayout/android.view.ViewGroup/android.widget'
                           '.TextView[1]')).should(have.text(value))
        return self
