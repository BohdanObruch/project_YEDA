import time
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


class SearchTaxi:

    def checking_sign_in_or_create_an_account_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        return self

    def close_rewards_and_wallet_message(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
        browser.driver.swipe(720, 683, 720, 2070, 400)
        return self

    def scroll_and_go_to_the_taxi_page(self, value):
        browser.driver.swipe(975, 319, 141, 319, 400)
        time.sleep(1)
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                           '/android.widget.LinearLayout/android.widget.LinearLayout['
                           '2]/android.widget.FrameLayout['
                           '1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                           '/android.widget.LinearLayout[2]/android.widget.TextView')).should(have.text(value)).click()
        return self

    def checking_the_title_of_the_instructions(self, value):
        s((AppiumBy.ID, 'com.booking:id/splash_title')).should(have.text(value))
        return self

    def skip_instructions(self):
        s((AppiumBy.ID, 'com.booking:id/skip_text')).click()
        return self

    def book_taxi(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout['
                           '2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget'
                           '.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.RelativeLayout[2]/javaClass/android.widget.EditText')).click()
        return self

    def checking_the_title_route_planner_page(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.RelativeLayout/android.widget.LinearLayout'
                           '/android.view.ViewGroup/android.widget.LinearLayout/android.widget'
                           '.TextView'))
        return self

    def input_start_location_and_select_from_the_list(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.RelativeLayout/android.widget.RelativeLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.RelativeLayout[2]/javaClass/android.widget.EditText')).type(value)

        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.RelativeLayout/android.widget.RelativeLayout'
                           '/android.widget.RelativeLayout/androidx.recyclerview.widget'
                           '.RecyclerView/android.widget.RelativeLayout[3]')).click()
        return self

    def input_final_location_and_select_from_the_list(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.RelativeLayout/android.widget.RelativeLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.RelativeLayout[3]/javaClass/android.widget.EditText')).type(value)

        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.RelativeLayout/android.widget.RelativeLayout'
                           '/android.widget.RelativeLayout/androidx.recyclerview.widget'
                           '.RecyclerView/android.widget.RelativeLayout[3]')).click()
        return self

    def select_date_and_time(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.view.ViewGroup/android.widget.LinearLayout/android'
                           '.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView')).click()
        return self

    def change_the_default_day(self):
        s((AppiumBy.ID, 'com.booking:id/current_date')).click()
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup'
                           '/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget'
                           '.LinearLayout/android.widget.GridView/android.widget.TextView[39]')).click()

        s((AppiumBy.ID, 'com.booking:id/confirm_button')).click()
        s((AppiumBy.ID, 'com.booking:id/search_return_taxis_button')).click()
        return self

    def search_taxi(self, value):
        s((AppiumBy.ID, 'com.booking:id/search_taxis_button')).click()
        s((AppiumBy.ID, 'com.booking:id/confirm_provider_later_text')).should(have.text(value))
        return self
