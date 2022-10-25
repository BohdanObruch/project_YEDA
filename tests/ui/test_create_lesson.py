import time
import pytest

from selene import have
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource
from yeda_admin_panel_tests import command
from allure import title, tag, step


@tag("Web UI")
@title("Creating an lesson and filling it with information")
def test_add_lesson(setup_browser):
    # browser = setup_browser

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the lesson page"):
        browser.element('.elearning-nav-li').click()
        browser.element('.lessons-nav-li').click()
        browser.element('.page-header').with_(timeout=4).should(have.text('Lessons'))

    with step("Creating a lesson"):
        browser.element('.panel-heading .btn').click()

        with step("Checking the Adding Lesson page display"):
            browser.element('.page-header').with_(timeout=4).should(have.text('Adding Lesson'))

        with step("Changing the status to active to display on the site"):
            browser.element('#dropdownMenuButton').click()
            browser.element('[data-status-id="3"]').click()

        with step("Choose a category"):
            browser.element('#dropdown-category').click()
            browser.element('[data-category-id="115"]').click()

        with step("Adding price"):
            browser.element('[name="normal_price"]').type('100')
            browser.element('[name="discount_price"]').type('75')

        with step("Filling in the Lesson Details"):
            with step("Filling in the title"):
                browser.element('.form-group #title').type('Microeconomics - lesson 1')

            with step("Filling content of lesson"):
                browser.element('.jodit-workplace .jodit-wysiwyg').type(
                    'The return curve - first part. The structure of the curve based on the factors of '
                    'production. Allocation of factors of production according to the principle of '
                    'comparative advantage.')

    with step("Submit the form"):
        browser.element('#save-lesson').click()

        with step("Specifying the 'Show date edited' checkbox"):
            browser.element('#show_date_edited').click()

        with step("Adding files"):
            browser.element('.lesson-files-block #lesson_files_input').send_keys(resource('Document_1.pdf'))
            browser.element('#files-tbody .file-to-speech').click()
            browser.element('.lesson-files-block #lesson_files_input').send_keys(resource('schedule.xlsx'))

    with step("Editing lesson"):
        with step("Adding lecturer"):
            browser.element('.lector-name').type('אולגה מסקרפונה')
            time.sleep(2)
            browser.element('.suggestions [data-id="48"]').click()
            browser.element('.add_lecturer').click()

        with step("Adding part of lesson"):
            with step("Adding Part #1"):
                browser.element('.add-video').click()
                browser.element('.open-video-collapse .lesson-part-toggle').click()

                with step("Filling in the title"):
                    browser.element('#lesson_part1 .page_video_title').type('Microeconomics lesson 1 - part A')

                with step("Adding video"):
                    browser.element('.lesson_video_file').send_keys(resource('Mathematics.mp4'))

                with step("Mark indications 'Speech from a summary'"):
                    with step("Specifying the 'Text to Speech' checkbox"):
                        browser.element('.checkbox-span .summary_to_speech_input').click()

                    with step("Mark indications 'Don't show the About text'"):
                        browser.element('.hide_text_if_there_is_speech_input').click()

                with step("Checking the video upload"):
                    browser.element('#save-lesson').perform(command.js.scroll_into_view)
                    browser.element('.vimeo_transcoding_text').with_(timeout=15) \
                        .should(have.text('Video was uploaded and is '
                                          'being transcoded by '
                                          'vimeo.\nThis may take some '
                                          'time.\nYou can save now and '
                                          'check for image later.'))

            with step("Save part lesson #1"):
                browser.element('#save-lesson').click()

            with step("Close the block part of the lesson #1"):
                browser.element('.open-video-collapse .lesson-part-toggle').click()

            with step("Adding part #2"):
                browser.element('.add-video').perform(command.js.click)
                time.sleep(1)
                browser.element('.lesson-video:nth-child(2) .lesson-part-toggle').click()

                with step("Filling in the title"):
                    browser.element('.lesson-video:nth-child(2) .page_video_title') \
                        .type('Microeconomics Lesson 1 - Part B')

                with step("Adding video"):
                    browser.element('.lesson-video:nth-child(2) .lesson_video_file') \
                        .send_keys(resource('Mathematics2.mp4'))

                with step("Checking the video upload"):
                    browser.element('#save-lesson').perform(command.js.scroll_into_view)
                    browser.element('.lesson-video:nth-child(2) .vimeo_transcoding_text').with_(timeout=15). \
                        should(have.text('Video was uploaded and is '
                                         'being transcoded by '
                                         'vimeo.\nThis may take some '
                                         'time.\nYou can save now and '
                                         'check for image later.'))

            with step("Save part lesson #2"):
                browser.element('#save-lesson').click()

            with step("Close the block part of the lesson #2"):
                browser.element('.lesson-video:nth-child(2) .lesson-part-toggle').click()

        with step("Moving blocks of parts of lessons between themselves"):
            time.sleep(1)
            first_part = browser.element('#lesson_parts_accordion .lesson-video:nth-child(1) .col')
            second_part = browser.element('#lesson_parts_accordion .lesson-video:nth-child(2) .lesson-video-handle')
            second_part.perform(command.drag_to(first_part))
            browser.element('#save-lesson').click()

        with step("Deleting a created lesson"):
            with step("Go to the Lessons page"):
                browser.element('.lessons-nav-li').click()

            with step("Search for a created lesson and delete it"):
                browser.element('[data-name="title"').type('Microeconomics - lesson 1')
                browser.element('.ui-sortable-handle .col').with_(timeout=6).should(have.text('Microeconomics - '
                                                                                              'lesson 1'))
                browser.element('.ui-sortable-handle .delete').click()
                browser.element('.container .btn:nth-child(1)').click()

            with step("Display a push message about successful removal of the lesson"):
                browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('Lesson has been deleted'))
