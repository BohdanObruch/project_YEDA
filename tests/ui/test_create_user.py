import calendar
import time

from selene import have
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel

current_GMT = time.gmtime()

ts = calendar.timegm(current_GMT)
name = ('Anna'+str(ts))

email = (name+'@gmail.com')

phone = ts


def test_add_user(setup_browser):
    # browser = setup_browser

    authorization_on_admin_panel()

    browser.element('.users-nav-li').click()

    browser.element('.page-header').should(have.text('Manage users'))

    browser.element('[data-target="#create-user-modal"').click()
    browser.element('.modal-title').should(have.text('ADD NEW USER'))
    browser.element('#app-user-form #edit_username').type(f'{name}')
    browser.element('#app-user-form #edit_name').type(f'{name}')
    browser.element('#app-user-form #edit_email').type(f'{email}')
    browser.element('#app-user-form #edit_phone').type('05310124711')
    browser.element('#app-user-form #edit_city').type('Krakow')
    browser.element('#app-user-form #password').type(f'{ts}')
    browser.element('#app-user-form #password_auth').type(f'{ts}')
    browser.element('[type="submit"]').click()
    browser.element('[data-notify="message"]').with_(timeout=20).should(have.text('New user has been created'))
    time.sleep(3)

    # Delete
    browser.element('.filter #search_text').type(f'{name}')

    panel = browser.element('.table')
    panel.all('tr').element_by_its('.username', have.exact_text(f'{name}')).element('.delete').click()
    browser.element('.container .btn:nth-child(1)').click()
    browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('User has been deleted'))
