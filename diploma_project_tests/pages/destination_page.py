from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared.jquery_style import s, ss


class SearchDestination:
    def enter_destination(self, value):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_destination')).click()
        s((AppiumBy.ID, 'com.booking:id/facet_with_bui_free_search_booking_header_toolbar_content')).type(value)
        return self

    def checking_the_availability_of_results(self, value):
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

    def checking_the_calendar_display(self):
        s((AppiumBy.ID, 'com.booking:id/calendar_week_days')).should(be.visible)
        return self

    def add_date_of_arrival(self):
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="18 November 2022"]')).click()
        return self

    def add_departure_date(self):
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="27 November 2022"]')).click()
        return self

    def check_the_dates(self, value):
        s((AppiumBy.ID, 'com.booking:id/facet_date_picker_selection_summary')).should(have.text(value))
        return self

    def confirm_the_choice_of_dates(self):
        s((AppiumBy.ID, 'com.booking:id/facet_date_picker_confirm')).click()
        return self

    def open_block_select_rooms_and_guests(self):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_accommodation_occupancy')).click()
        return self

    def check_block_select_rooms_and_guests(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.LinearLayout/android.widget.LinearLayout/android.widget.TextView')) \
            .should(have.text(value))
        return self

    def change_number_of_guests_and_rooms(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup['
                           '2]/android.widget.LinearLayout/android.widget.Button[1]')).click()
        return self

    def apply_changes(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.LinearLayout/android.widget.RelativeLayout')).click()
        return self

    def search_for_housing(self):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_cta')).click()
        return self

    def checking_the_block_title(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.TextView[1]')).should(have.text(value))
        return self

    def close_welcome_block(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.Button')).click()
        return self

    def checking_the_results_of_a_given_search(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout '
                           '/android.view.ViewGroup/android.widget.FrameLayout/android.widget'
                           '.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx'
                           '.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                           '1]/android.view.ViewGroup/android.widget.TextView[1]')) \
            .should(have.text(value))
        return self
