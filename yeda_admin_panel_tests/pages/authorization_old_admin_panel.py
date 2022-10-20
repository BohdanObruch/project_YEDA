import time

from tests.conftest import *


def authorization_on_admin_panel():
    opened_page_admin_panel()
    # time.sleep(5)

    login = browser.element('#username')
    login.type('Test12')

    password = browser.element('#password')
    password.type('123456')

    browser.element('[type="submit"]').click()


