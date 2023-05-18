from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared.jquery_style import s
from diploma_project_tests.command import swipe_helper


class SearchTaxiPage:

    def checking_sign_in_or_create_an_account_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        return self

    def close_rewards_and_wallet_message(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
        swipe_helper.swipe_to_close_wallet_message()
        return self

    def scroll_and_go_to_the_taxi_page(self, value):
        swipe_helper.swipe_to_right()
        s((AppiumBy.XPATH, '//*[@text="Taxi"]')).with_(timeout=2).should(have.text(value)).click()
        return self

    def checking_the_title_of_the_instructions(self, value):
        s((AppiumBy.ID, 'com.booking:id/splash_title')).should(have.text(value))
        return self

    def skip_instructions(self):
        s((AppiumBy.ID, 'com.booking:id/skip_text')).click()
        return self

    def book_taxi(self):
        s((AppiumBy.XPATH, '//*[@text="Enter pick-up location"]')).click()
        return self

    def checking_the_title_route_planner_page(self, value):
        s((AppiumBy.XPATH, '//*[@text="Route planner"]')).should(have.text(value))
        return self

    def input_start_location_and_select_from_the_list(self, value):
        s((AppiumBy.XPATH, '//*[@text="Enter pick-up location"]')).type(value)

        s((AppiumBy.XPATH, '//*[@text="Igor Sikorsky Kyiv International Airport"]')).with_(timeout=5).click()
        return self

    def input_final_location_and_select_from_the_list(self, value):
        s((AppiumBy.XPATH, '//*[@text="Enter destination"]')).type(value)
        s((AppiumBy.XPATH, '//*[@text="DREAM Hostel Kyiv"]')).with_(timeout=5).click()
        return self

    def select_date_and_time(self):
        s((AppiumBy.XPATH, '//*[@text="Choose your pick-up time"]')).click()
        return self

    def change_the_default_day(self):
        s((AppiumBy.ID, 'com.booking:id/current_date')).click()
        s((AppiumBy.ID, 'com.booking:id/calendar_view_right_arrow')).click()
        s((AppiumBy.XPATH, '//*[@text="16"]')).click()
        s((AppiumBy.ID, 'com.booking:id/confirm_button')).click()
        s((AppiumBy.ID, 'com.booking:id/search_return_taxis_button')).click()
        return self

    def search_taxi(self, value):
        s((AppiumBy.ID, 'com.booking:id/search_taxis_button')).click()
        s((AppiumBy.ID, 'com.booking:id/ukraine_banner_title')).with_(timeout=5).should(have.text(value))
        return self
