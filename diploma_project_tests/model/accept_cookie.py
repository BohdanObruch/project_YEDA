from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step


def accept_cookie_settings():
    with step('Checking the display Cookie settings page'):
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                         '/android.view.ViewGroup/android.widget.TextView')).should(have.text('Cookie '
                                                                                                              'settings'))
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                         '/android.view.ViewGroup/android.widget.Button[1]')).click()
