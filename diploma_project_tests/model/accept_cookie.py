from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from allure import step
from selene.support.shared.jquery_style import s, ss


def accept_cookie_settings():
    with step('Checking the display Cookie settings page'):
        s((AppiumBy.XPATH, '//*[@text="Cookie settings"]')).should(have.text('Cookie settings'))
        s((AppiumBy.XPATH, '//*[@text="Accept"]')).click()
