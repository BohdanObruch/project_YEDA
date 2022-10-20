import time

from selene.core.entity import Element
from selene.support.shared import browser

from tests.conftest import *


def authorization_on_the_site():
    opened_page_website()
    # time.sleep(5)

    browser.element('[href="/auth/login"]').click()

    login = browser.element('#username')
    login.type('admin12')  #Test12 #123456789

    password = browser.element('#password')
    password.type('123456')

    browser.element('[airloadwhen="login"]').click()

    browser.element('#to-admin-button').with_(timeout=8).click()





