import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


class SearchAttractionsPage:
    def close_authorization_and_registration_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        return self

    def close_rewards_and_wallet_message(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
        browser.driver.swipe(720, 683, 720, 2070, 400)
        time.sleep(1)
        return self

    def scroll_and_go_to_the_attractions_page(self, value):
        browser.driver.swipe(913, 319, 141, 319, 400)
        time.sleep(1)
        s((AppiumBy.XPATH, '//*[@text="Attractions"]')).should(have.text(value)).click()
        return self

    def checking_the_title_of_the_search_attractions(self, value):
        s((AppiumBy.XPATH, '//*[@text="Find and book a great experience"]')).should(have.text(value)).click()
        return self

    def add_locating(self, value):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_basic_field_label')).click()
        s((AppiumBy.CLASS_NAME, 'android.widget.EditText')).type(value)
        s((AppiumBy.XPATH, '//*[@text="Kyiv, Ukraine"]')).click()
        return self

    def add_date(self):
        s((AppiumBy.XPATH, '//*[@text="Any dates"]')).click()

        s((AppiumBy.XPATH, '//*[contains(@content-desc, "09")]')).click()
        s((AppiumBy.XPATH, '//*[contains(@content-desc, "18")]')).click()
        s((AppiumBy.ID, 'com.booking:id/facet_date_picker_confirm')).click()
        return self

    def search_attractions(self):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_cta')).click()
        s((AppiumBy.XPATH, '//*[contains(@text, "things to do")]')).should(be.visible)
        return self
