import time
import pytest
import os

from selene import have, command
from selene.support.shared import browser  # убрать если нужен запуск удаленно
from yeda_admin_panel_tests.controls.utils import resource
from yeda_admin_panel_tests.pages.authorization_website import authorization_on_the_site
from yeda_admin_panel_tests.controls.utils import resource
from allure import title, tag, step


@tag("Web UI")
@title("Creating an course")
def test_create_course(setup_browser):
    # browser = setup_browser # розкамитить если нужен запуск удаленно
    NAME_COURSE = os.getenv('name_course')
    URL_COURSES = os.getenv('url_courses')

    with step("Authorization on the site and go to the admin panel"):
        authorization_on_the_site()

    with step("Go to the courses page"):
        browser.element('[href="/admin/courses"]').click()

    with step("Creating a course"):
        browser.element('[yedaoldadminhref="elearning/courses/create"]').click()

        with step("Changing the status to active to display on the site"):
            browser.element('#dropdownMenuButton').click()
            browser.element('[data-status-id="3"]').click()

        with step("Choose a category"):
            browser.element('#dropdown-category').click()
            browser.element('[data-category-id="115"]').click()

        with step("Filling in the name of the course"):
            browser.element('#name').type(f'{NAME_COURSE}')

        with step("Generate slug"):
            browser.element('#generate-slug').click()
            # browser.element('#slug').should(have.exact_texts('qa-automation-course'))

        with step("Filling in the short description"):
            browser.element('[name="short_descr"]').type('This course about how to learn QA Automation')

        with step("Adding a description"):
            browser.element('[name="descr"]').type('This course about how to learn QA Automation')

        with step("Filling in the duration"):
            browser.element('[name="duration"]').type('12 month')

        with step("Filling in the prerequisites"):
            browser.element('[name="prerequisites"]').type('Not have')

        with step("Adding video to the 'Video or image' block"):
            browser.element('[name="video_link"]').type('https://vimeo.com/437087249')

        with step("Adding teaser images"):
            browser.element('#course_photo').send_keys(resource('circle.png'))

        with step("Adding description"):
            browser.element('.jodit-wysiwyg').type('QA Automation').press_enter()
            browser.element('.jodit-wysiwyg').type('This course about how to learn QA').press_enter()
            browser.element('.panel-body .jodit-status-bar__item .jodit-toolbar-button__button').click()
            browser.element('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()

        with step("Associated files"):
            with step("Displaying files only for students of the course"):
                browser.element('[name="show_files_to_students"]').click()

            with step("Adding files"):
                browser.element('#files_input').send_keys(resource('template-courses.xlsx'))
                browser.element('#files_input').send_keys(resource('lesson_19.pdf'))
                time.sleep(2)

        with step("Adding SEO"):
            with step("Filling Title"):
                browser.element('[name="meta_title"]').type('QA Automation')

            with step("Filling Description"):
                browser.element('[name="meta_description"]').type('This course about how to learn QA Automation')

            with step("Filling Author"):
                browser.element('[name="meta_author"]').type('QA')

        with step("Adding start date"):
            browser.element('#date_begin_date').type('2023-01-01').press_tab()

        with step("Adding end date"):
            browser.element('#date_end_date').type('2023-02-28').press_tab()

        with step("Adding price"):
            browser.element('[name="normal_price"]').type('100')
            browser.element('[name="discount_price"]').type('60')

    with step("Submit the form"):
        browser.element('[type="submit"]').click()

    with step("Checking page title changes on the Editing Course"):
        browser.element('.page-header').with_(timeout=10).should(have.text('Editing Course'))

    with step("Deleting a created Course"):
        with step("Go to the page with all the courses"):
            browser.element(f'[href="{URL_COURSES}"]').perform(command.js.click)
            browser.element('#portal-header-default').with_(timeout=10).should(have.text('Courses'))

        with step("Search for a created course and delete it"):
            table = browser.element('#cdk-drop-list-0')
            table.all('.air-list-item').element_by_its('[airtablelikecell="course-name"]',
                                                       have.exact_text(f'{NAME_COURSE}')) \
                .element('.color-danger.clear').click()
            browser.element('// *[text() = "Confirm delete"]').click()
            time.sleep(2)

        with step("Checking that the created course has been deleted"):
            table = browser.element('#cdk-drop-list-0')
            table.all('.air-list-item').element_by_its('[airtablelikecell="course-name"',
                                                       not have.exact_text(f'{NAME_COURSE}'))
