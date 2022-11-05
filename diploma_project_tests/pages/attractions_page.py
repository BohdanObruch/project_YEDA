import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


class SearchAttractions:
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
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                           '/android.widget.LinearLayout/android.widget.LinearLayout['
                           '2]/android.widget.FrameLayout['
                           '1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                           '/android.widget.LinearLayout[3]/android.widget.TextView')).should(have.text(value)).click()
        return self

    def checking_the_title_of_the_search_attractions(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.LinearLayout[2]/android.widget.TextView')).should(have.text(value)).click()
        return self

    def add_locating(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.LinearLayout['
                           '2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget'
                           '.LinearLayout[1]/android.widget.TextView')).click()
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui'
                           '.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText'
                           '')).type(value)
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                           '.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android'
                           '.view.View/android.view.View/android.view.View/android.view.View['
                           '1]')).click()
        return self

    def add_date(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.LinearLayout['
                           '2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget'
                           '.LinearLayout[2]/android.widget.TextView')).click()

        s((AppiumBy.XPATH, '//android.view.View[@content-desc="09 November 2022"]')).click()
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="18 November 2022"]')).click()
        s((AppiumBy.ID, 'com.booking:id/facet_date_picker_confirm')).click()
        return self

    def search_attractions(self):
        s((AppiumBy.ID, 'com.booking:id/facet_search_box_cta')).click()
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                           '/android.widget.LinearLayout/android.widget.TextView')).should(be.visible)
        return self
