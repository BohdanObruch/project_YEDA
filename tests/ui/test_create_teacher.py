import time
import calendar

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource


current_GMT = time.gmtime()

ts = calendar.timegm(current_GMT)
name = ('Pavel'+str(ts))

email = (name+'@gmail.com')

phone = ts


def test_add_teacher(setup_browser):
    # browser = setup_browser

    authorization_on_admin_panel()

    browser.element('.elearning-nav-li').click()
    browser.element('.teachers-nav-li').click()

    browser.element('.page-header').with_(timeout=4).should(have.text('Teachers'))

    browser.element('.panel-heading .btn').click()

    browser.element('.page-header').with_(timeout=4).should(have.text('Create Teacher'))
    browser.element('.upload_button #photo').send_keys(resource('Albert_Einstein.png'))
    browser.element('#seo-collapse [name="meta_title"]').type('SEO Title')
    browser.element('#seo-collapse [name="meta_description"]').type('SEO Description')
    browser.element('#name').type(name)

    browser.element('[name="positions"]').type('Professor of the highest category')
    browser.element('[name="short_descr"]').type('Lecturer for the economy')
    browser.element('[name="about"]').type('Expert in everything related to security, political, family and black '
                                           'economy')
    browser.element('[name="email"]').type(email)
    browser.element('[name="phone"]').type(phone)
    browser.element('[type="submit"]').click()
    time.sleep(10)
    browser.element('.teachers-nav-li').click()

    browser.element('.filter #search_text').type(name).press_enter()
    browser.element(f'//*[text() = "{name}"]').with_(timeout=5).should(have.text(name))

    # delete

    browser.all('.table').element_by_its('.teacher-name', have.exact_text(name)).element('.delete').click()
    browser.element('.container .btn:nth-child(1)').click()
    browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('Teacher has been deleted'))
