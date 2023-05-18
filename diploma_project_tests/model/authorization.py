from selene import be
from tests.conftest import *
from selene.support.shared.jquery_style import s

login_admin = dotenv.get('LOGIN_ADMIN')
admin_password = dotenv.get('ADMIN_PASSWORD')


def authorization_on_admin_panel():
    opened_page_admin_panel()
    s('#username').type(f'{login_admin}')
    s('#password').type(f'{admin_password}')
    s('[type="submit"]').click()


def authorization_on_the_site():
    opened_page_website()
    s('[href="/auth/login"]').with_(timeout=10).click()
    s('#username').type(f'{login_admin}')

    s('#password').type(f'{admin_password}')
    s('[airloadwhen="login"]').click()
    s('[href="/my-studies/my-courses/all"]').with_(timeout=10).should(be.visible)
    s('#to-admin-button').should(be.visible).double_click()
