import calendar
import time

from selene import have
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from allure import title, tag, step


@tag("Web UI")
@title("Creating user")
def test_add_user(setup_browser):
    current_GMT = time.gmtime()

    ts = calendar.timegm(current_GMT)
    name = ('Anna' + str(ts))
    email = (name + '@gmail.com')
    phone = ts

    # browser = setup_browser
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the Users page"):
        browser.element('.users-nav-li').click()

    with step("Checking the 'Manage users' page display"):
        browser.element('.page-header').should(have.text('Manage users'))

    with step("Creating user"):
        browser.element('[data-target="#create-user-modal"').click()

        with step("Checking the 'ADD NEW USER' pop-up display"):
            browser.element('.modal-title').should(have.text('ADD NEW USER'))

        with step("Filling username"):
            browser.element('#app-user-form #edit_username').type(f'{name}')

        with step("Filling name"):
            browser.element('#app-user-form #edit_name').type(f'{name}')

        with step("Filling email"):
            browser.element('#app-user-form #edit_email').type(f'{email}')

        with step("Filling phone number"):
            browser.element('#app-user-form #edit_phone').type('05310124711')

        with step("Filling living area"):
            browser.element('#app-user-form #edit_city').type('Krakow')

        with step("Filling password"):
            browser.element('#app-user-form #password').type(f'{ts}')

        with step("Filling repeat password"):
            browser.element('#app-user-form #password_auth').type(f'{ts}')

        with step("Submit the form"):
            browser.element('[type="submit"]').click()

        with step("Display a push message about successful create user"):
            browser.element('[data-notify="message"]').with_(timeout=20).should(have.text('New user has been created'))
            time.sleep(3)

    with step("Deleting a created user"):
        browser.element('.filter #search_text').type(f'{name}')

        with step("Search for a created user and delete it"):
            panel = browser.element('.table')
            panel.all('tr').element_by_its('.username', have.exact_text(f'{name}')).element('.delete').click()
            browser.element('.container .btn:nth-child(1)').click()

        with step("Display a push message about successful removal of the user"):
            browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('User has been deleted'))
