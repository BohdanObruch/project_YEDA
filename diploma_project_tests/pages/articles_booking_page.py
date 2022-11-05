import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


class SearchArticles:

    def checking_sign_in_or_create_an_account_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        return self

    def close_rewards_and_wallet_message(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
        browser.driver.swipe(720, 683, 720, 2070, 400)
        return self

    def scroll_and_go_to_the_articles_page(self):
        browser.driver.swipe(470, 1400, 470, -500, 330)
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                           '2]/android.widget.FrameLayout['
                           '1]/android.widget.LinearLayout/androidx.compose.ui.platform.ComposeView'
                           '/android.view.View/android.view.ViewGroup/android.widget.FrameLayout'
                           '/androidx.compose.ui.platform.ComposeView/android.view.View/android'
                           '.widget.ScrollView/android.view.View[5]/android.view.View')).should(be.visible).click()
        return self

    def checking_the_display_on_the_article_page(self, value):
        s((AppiumBy.XPATH, '//android.view.View[@content-desc="Travel articles"]/android.widget.TextView')) \
            .should(have.text(value))
        time.sleep(1)
        return self

    def manage_cookie_preferences(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView'
                           '/android.webkit.WebView/android.view.View/android.view.View['
                           '3]/android.view.View/android.view.View/android.view.View/android.view'
                           '.View[1]/android.view.View/android.widget.TextView[1]')).should(have.text(value))

        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView'
                           '/android.webkit.WebView/android.view.View/android.view.View['
                           '3]/android.view.View/android.view.View/android.view.View/android.view'
                           '.View[2]/android.view.View/android.widget.Button[2]')).click()
        time.sleep(1)
        return self

    def checking_the_availability_of_the_article_and_opening_it(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                           '.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android'
                           '.view.View[2]/android.view.View[2]/android.view.View[1]')).click()
        time.sleep(1)
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                           '.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android'
                           '.view.View[2]/android.view.View[1]/android.widget.ListView')).should(be.visible)
        return self
