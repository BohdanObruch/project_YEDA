import time

from tests.conftest import *
from selene.core.entity import Element
from selene.support.shared import browser


def authorization_on_admin_panel():
    opened_page_admin_panel()
    # time.sleep(5)
    login = browser.element('#username')
    login.type('dimalebid')

    password = browser.element('#password')
    password.type('123456')

    browser.element('[type="submit"]').click()


def authorization_on_the_site():
    opened_page_website()
    # time.sleep(5)
    browser.element('[href="/auth/login"]').click()
    login = browser.element('#username')
    login.type('dimalebid')  #Test12 #123456789

    password = browser.element('#password')
    password.type('123456')

    browser.element('.center .air-h1').click()
    browser.element('[airloadwhen="login"]').click()
    browser.element('#to-admin-button').with_(timeout=8).click()