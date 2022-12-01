import time
import calendar
import secrets
import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

password_length = 13
current_GMT = time.gmtime()
ts = calendar.timegm(current_GMT)
password = secrets.token_urlsafe(password_length)
name = ''.join(random.choices((string.ascii_uppercase + string.ascii_lowercase), k=5))
login_name = (name + str(ts))
email = (login_name + '@gmail.com')


class RegistrationUserPage:
    def checking_sign_in_page(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        return self

    def click_create_account(self):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.LinearLayout/android.widget.FrameLayout/android'
                           '.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                           '.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout['
                           '2]/android.widget.FrameLayout/android.widget.Button')).click()
        return self

    def input_email(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.ID, 'com.booking:id/identity_text_input_edit_text')).type(email)
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.LinearLayout/android.widget.FrameLayout/android'
                           '.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.widget.Button')).click()
        return self

    def input_password(self, value):
        s((AppiumBy.ID, 'com.booking:id/identity_header_title')).should(have.text(value))
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.LinearLayout/android.widget.FrameLayout/android'
                           '.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                           '.LinearLayout['
                           '2]/android.widget.LinearLayout/android.widget.FrameLayout/android'
                           '.widget.EditText')).type(password)
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout['
                           '2]/android.widget.LinearLayout/android.widget.FrameLayout/android'
                           '.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                           '.LinearLayout['
                           '4]/android.widget.LinearLayout/android.widget.FrameLayout/android'
                           '.widget.EditText')).type(password)
        return self

    def click_create_account_and_sign_in(self):
        s((AppiumBy.ID, 'com.booking:id/identity_landing_social_button_text')).click()
        return self

    def checking_notification(self, value):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text(value))
        time.sleep(2)
        return self

    def start_searching(self):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_primary_action')).click()
        time.sleep(2)
        return self

    def checking_displaying_main_page(self, value):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                           '.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout['
                           '1]/android.widget.LinearLayout/androidx.compose.ui.platform.ComposeView/android.view.View'
                           '/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform'
                           '.ComposeView/android.view.View/android.widget.ScrollView/android.view.ViewGroup['
                           '1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout['
                           '1]/android.widget.TextView')).should(have.text(value))
        return self
