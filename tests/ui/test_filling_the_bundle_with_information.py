import time
import os

from selene import have, command
from selene.support.shared import browser
from diploma_project_tests.model.authorization import authorization_on_admin_panel
from allure import title, tag, step
from diploma_project_tests.helpers import app
from diploma_project_tests.data.data import *


@tag("Web UI")
@title("Filling in the created bundle")
def test_filling_the_bundle(setup_browser):
    # browser = setup_browser

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the bundle page"):
        app.filling_bundles.open_bundles_page('Bundles')

    with step("Open the created bundle"):
        app.filling_bundles.open_create_bundle()

        with step("Checking that the bundle is open"):
            app.filling_bundles.checking_editing_bundle_page(' Editing Bundle')

        with step("Opening the Students block and adding students"):
            app.filling_bundles.add_students(Bundles.file_with_users)

        with step("Opening the Courses block and adding courses"):
            app.filling_bundles.open_courses_block()

            with step("Adding course #1"):
                app.filling_bundles.add_first_course(Bundles.name_first_course, Bundles.full_name_first_course)

            with step("Indication of the mark that the mandatory course"):
                app.filling_bundles.mark_that_the_mandatory_first_course()

            with step("Specify the date when the course will be available"):
                app.filling_bundles.date_when_first_course_available()

            with step("Specify the date when access to the course will be closed"):
                app.filling_bundles.date_when_first_course_be_closed(Bundles.date_closed_first_course)

            with step("Adding course #2"):
                app.filling_bundles.add_second_course(Bundles.name_second_course, Bundles.full_name_second_course)

            with step("Indication of the mark that the mandatory course"):
                app.filling_bundles.mark_that_the_mandatory_second_course()

            with step("Specify the date when the course will be available"):
                app.filling_bundles.date_when_second_course_available()

            with step("Specify the date when access to the course will be closed"):
                app.filling_bundles.date_when_second_course_be_closed(Bundles.date_closed_second_course)

    with step("Deleting a created bundle"):
        with step("Go to the page with all the bundles"):
            app.filling_bundles.open_all_bundles_page('Bundles')

        with step("Search for a created bundle and delete it"):
            app.filling_bundles.search_created_bundle_and_delete()

        with step("Display a push message about successful removal of the bundle"):
            app.filling_bundles.push_message_about_successful_removal_bundle('Bundle has been deleted')
