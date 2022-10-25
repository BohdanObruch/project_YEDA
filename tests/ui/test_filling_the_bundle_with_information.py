import time
import pytest
import os

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource
from allure import title, tag, step


@tag("Web UI")
@title("Filling in the created bundle")
def test_filling_the_bundle(setup_browser):
    # browser = setup_browser
    NAME_BUNDLE = os.getenv('name_bundle_ui')
    URL_BUNDLES = os.getenv('url_bundles')

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the bundle page"):
        browser.element(f'[href="{URL_BUNDLES}"]').click()
        browser.element('.page-header').should(have.text('Bundles'))

    with step(f"Open the created bundle - {NAME_BUNDLE}"):
        browser.element(f'//*[text() = "{NAME_BUNDLE}"]').click()  # QA Bundle

        with step("Checking that the bundle is open"):
            browser.element('.page-header').should(have.text(' Editing Bundle'))

        with step("Opening the Students block and adding students"):
            browser.element('.panel [data-target="#students-collapse"] .fa-plus').click()
            browser.element('#students-collapse #import_users_file').send_keys(resource('template-courses.xlsx'))
            browser.element('.import-student:nth-child(1) .remove-from-import').click()
            browser.element('.jconfirm-buttons .btn-default:nth-child(1)').click()
            browser.element('.import-student:nth-child(3) .remove-from-import').click()
            browser.element('.jconfirm-buttons .btn-default:nth-child(1)').click()
            browser.element('.students-import #import-students').click()
            time.sleep(4)

        with step("Opening the Courses block and adding courses"):
            browser.element('.panel [data-target="#courses-collapse"] .fa-plus').click()

            with step("Adding course #1"):
                browser.element('.forum-form #find-course').type('קורס מאקרו כלכלה')
                browser.element('.forum-form #course-suggestions').element('[data-id="196"]').click()
                browser.element('#courses-collapse #add-course').click()
                browser.element('#bundle-course-item-196 .text-right').with_(timeout=3)\
                    .should(have.text('קורס מאקרו כלכלה קורס מאקרו כלכלה'))
            with step("Indication of the mark that the mandatory course"):
                browser.element('#bundle-course-item-196 .course-is-required').click()

            with step("Specify the date when the course will be available"):
                browser.element('#bundle-course-item-196 .date-start-bundle-course').click()
                browser.element('.ui-datepicker-next').click().element('//*[text() = "29"]').click() #October 29

            with step("Specify the date when access to the course will be closed"):
                browser.element('#bundle-course-item-196 .date-end-bundle-course').click()
                browser.element('.ui-datepicker-next').click()
                # browser.element('.ui-datepicker-next').click()
                browser.element('//*[text() = "15"]').click() #November 15
                browser.element('#bundle-course-item-196 .date-end-bundle-course').with_(timeout=5).\
                    should(have.value('2022-11-15'))

            with step("Adding course #2"):
                browser.element('.forum-form #find-course').type('קורס מאקרו כלכלה')
                browser.element('.forum-form #course-suggestions').element('[data-id="195"]').click()
                browser.element('#courses-collapse #add-course').click()
                browser.element('#bundle-course-item-195 .text-right').with_(timeout=3)\
                    .should(have.text('קורס מאקרו כלכלה'))

            with step("Indication of the mark that the mandatory course"):
                browser.element('#bundle-course-item-195 .course-is-required').click()

            with step("Specify the date when the course will be available"):
                browser.element('#bundle-course-item-195 .date-start-bundle-course').click()
                browser.element('.ui-datepicker-next').click()
                # browser.element('.ui-datepicker-next').click()
                browser.element('//*[text() = "20"]').click() #November 20

            with step("Specify the date when access to the course will be closed"):
                browser.element('#bundle-course-item-195 .date-end-bundle-course').click()
                browser.element('.ui-datepicker-next').click()
                browser.element('.ui-datepicker-next').click()
                # browser.element('.ui-datepicker-next').click()
                browser.element('//*[text() = "10"]').click() #December 10
                browser.element('#bundle-course-item-195 .date-end-bundle-course').with_(timeout=5).\
                    should(have.value('2022-12-10'))

    with step("Deleting a created bundle"):
        with step("Go to the page with all the bundles"):
            browser.element(f'[href="{URL_BUNDLES}"]').perform(command.js.click)
            browser.element('.page-header').with_(timeout=7).should(have.text('Bundles'))

        with step("Search for a created bundle and delete it"):
            panel = browser.element('.panel-body')
            panel.all('.row').element_by_its('.course-link', have.exact_text(f'{NAME_BUNDLE}')).element('.delete')\
                .click()
            browser.element('.container .btn:nth-child(1)').click()

        with step("Display a push message about successful removal of the bundle"):
            browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('Bundle has been deleted'))
