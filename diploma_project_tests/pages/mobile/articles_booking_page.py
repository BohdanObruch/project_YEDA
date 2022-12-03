from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared.jquery_style import s, ss
from diploma_project_tests.command import swipe_helper


class SearchArticlesPage:

    def checking_sign_in_or_create_an_account_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        return self

    def close_rewards_and_wallet_message(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
        swipe_helper.swipe_to_close_wallet_message()
        return self

    def scroll_and_go_to_the_articles_page(self):
        swipe_helper.swipe_to_down()
        s((AppiumBy.XPATH, '//*[@text="Travel articles"]')).should(be.visible).click()
        return self

    def manage_cookie_preferences(self, value):
        s((AppiumBy.XPATH, '//*[@text="Manage cookie preferences"]')).with_(timeout=4).should(have.text(value))
        s((AppiumBy.XPATH, '//*[@text="Accept"]')).click()
        return self

    def checking_the_display_on_the_article_page(self, value):
        s((AppiumBy.XPATH, '//*[@content-desc="Travel articles"]/android.widget.TextView')).with_(timeout=3)\
            .should(have.text(value))
        return self

    def checking_the_availability_of_the_article_and_opening_it(self):
        s((AppiumBy.XPATH, '//android.view.View[2]/android.view.View[2]/android.view.View[1]')).with_(timeout=1).click()
        s((AppiumBy.XPATH, '//*[@content-desc="Articles"]/android.widget.TextView')).with_(timeout=2).should(be.visible)
        return self
