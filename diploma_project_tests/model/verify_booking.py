from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step
from selene.support.shared.jquery_style import s, ss


def verify_showing_welcome_message():
    with step('Checking the display of the notification'):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_title')).should(have.text('Welcome to Booking.com!'))

    with step('Start searching'):
        s((AppiumBy.ID, 'com.booking:id/bui_empty_state_primary_action')).click()


def verify_search_capability():
    with step('Displaying the main page and the ability to search'):
        s((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                         '/android.widget.LinearLayout/android.widget.LinearLayout['
                                         '2]/android.widget.FrameLayout['
                                         '1]/android.widget.LinearLayout/androidx.compose.ui.platform.ComposeView'
                                         '/android.view.View/android.view.ViewGroup/android.widget.FrameLayout'
                                         '/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget'
                                         '.ScrollView/android.view.ViewGroup['
                                         '1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                         '.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android'
                                         '.widget.LinearLayout[1]/android.widget.TextView')) \
            .should(have.text('Enter your destination'))
