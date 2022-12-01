import time

from tests.conftest import *
from selene.core.entity import Element
from selene.support.shared import browser
from dotenv import load_dotenv

login_admin = os.getenv('LOGIN_ADMIN')
admin_password = os.getenv('ADMIN_PASSWORD')


def authorization_on_admin_panel():
    opened_page_admin_panel()
    login = browser.element('#username')
    login.type(f'{login_admin}')

    password = browser.element('#password')
    password.type(f'{admin_password}')

    browser.element('[type="submit"]').click()


def authorization_on_the_site():
    opened_page_website()
    browser.element('[href="/auth/login"]').click()
    login = browser.element('#username')
    login.type(f'{login_admin}')

    password = browser.element('#password')
    password.type(f'{admin_password}')

    browser.element('.center .air-h1').click()
    browser.element('[airloadwhen="login"]').click()
    browser.element('#to-admin-button').with_(timeout=8).click()
