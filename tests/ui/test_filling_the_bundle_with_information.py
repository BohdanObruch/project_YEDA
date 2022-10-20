import time

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource
from tests.ui.test_create_bundles import name_bundle


def test_filling_the_bundle(setup_browser):
    # browser = setup_browser

    authorization_on_admin_panel()

    browser.element('[href="https://dev.biflow.co/collegeadmin/elearning/bundles"]').click()

    browser.element('.page-header').should(have.text('Bundles'))

    # name_bundle = "QA Bundle"

    browser.element(f'//*[text() = "{name_bundle}"]').click()  # QA Bundle

    browser.element('.page-header').should(have.text(' Editing Bundle'))

    # Students
    browser.element('.panel [data-target="#students-collapse"] .fa-plus').click()
    browser.element('#students-collapse #import_users_file').send_keys(resource('template-courses.xlsx'))
    browser.element('.import-student:nth-child(1) .remove-from-import').click()
    browser.element('.jconfirm-buttons .btn-default:nth-child(1)').click()
    browser.element('.import-student:nth-child(3) .remove-from-import').click()
    browser.element('.jconfirm-buttons .btn-default:nth-child(1)').click()
    browser.element('.students-import #import-students').click()
    time.sleep(5)

    # Courses
    browser.element('.panel [data-target="#courses-collapse"] .fa-plus').click()
    browser.element('.forum-form #find-course').type('קורס מאקרו כלכלה')
    browser.element('.forum-form #course-suggestions').element('[data-id="196"]').click()
    browser.element('#courses-collapse #add-course').click()
    browser.element('#bundle-course-item-196 .text-right').with_(timeout=3).should(have.text('קורס מאקרו כלכלה קורס '
                                                                                             'מאקרו כלכלה'))
    browser.element('#bundle-course-item-196 .course-is-required').click()
    browser.element('#bundle-course-item-196 .date-start-bundle-course').click()
    browser.element('.ui-datepicker-next').click().element('//*[text() = "29"]').click() #October 29
    browser.element('#bundle-course-item-196 .date-end-bundle-course').click()
    browser.element('.ui-datepicker-next').click()
    # browser.element('.ui-datepicker-next').click()
    browser.element('//*[text() = "15"]').click() #November 15
    browser.element('#bundle-course-item-196 .date-end-bundle-course').with_(timeout=5).should(have.value('2022-11-15'))

    browser.element('.forum-form #find-course').type('קורס מאקרו כלכלה')
    browser.element('.forum-form #course-suggestions').element('[data-id="195"]').click()
    browser.element('#courses-collapse #add-course').click()
    browser.element('#bundle-course-item-195 .text-right').with_(timeout=3).should(have.text('קורס מאקרו כלכלה'))
    browser.element('#bundle-course-item-195 .course-is-required').click()
    browser.element('#bundle-course-item-195 .date-start-bundle-course').click()
    browser.element('.ui-datepicker-next').click()
    # browser.element('.ui-datepicker-next').click()
    browser.element('//*[text() = "20"]').click() #November 20
    browser.element('#bundle-course-item-195 .date-end-bundle-course').click()
    browser.element('.ui-datepicker-next').click()
    browser.element('.ui-datepicker-next').click()
    # browser.element('.ui-datepicker-next').click()
    browser.element('//*[text() = "10"]').click() #December 10
    browser.element('#bundle-course-item-195 .date-end-bundle-course').with_(timeout=5).should(have.value('2022-12-10'))

    # delete bundle
    browser.element('[href="https://dev.biflow.co/collegeadmin/elearning/bundles"]').perform(command.js.click)
    browser.element('.page-header').with_(timeout=7).should(have.text('Bundles'))

    panel = browser.element('.panel-body')
    panel.all('.row').element_by_its('.course-link', have.exact_text(f'{name_bundle}')).element('.delete').click()

    browser.element('.container .btn:nth-child(1)').click()
    browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('Bundle has been deleted'))


