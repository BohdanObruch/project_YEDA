import time

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource


def test_add_lesson(setup_browser):
    # browser = setup_browser

    authorization_on_admin_panel()

    browser.element('.elearning-nav-li').click()
    browser.element('.lessons-nav-li').click()

    browser.element('.page-header').with_(timeout=4).should(have.text('Lessons'))

    browser.element('.panel-heading .btn').click()

    browser.element('.page-header').with_(timeout=4).should(have.text('Adding Lesson'))

    # Status
    browser.element('#dropdownMenuButton').click()
    browser.element('[data-status-id="3"]').click()

    # Category
    browser.element('#dropdown-category').click()
    browser.element('[data-category-id="115"]').click()  # QA

    # Price
    browser.element('[name="normal_price"]').type('100')
    browser.element('[name="discount_price"]').type('75')

    # Lesson Details

    # Name of the lesson
    browser.element('.form-group #title').type('Microeconomics - lesson 1')

    # Content of lesson
    browser.element('.jodit-workplace .jodit-wysiwyg').type(
        'The return curve - first part. The structure of the curve based on the factors of '
        'production. Allocation of factors of production according to the principle of '
        'comparative advantage.')

    # Save
    browser.element('#save-lesson').click()

    # Dates
    browser.element('#show_date_edited').click()

    # File
    browser.element('.lesson-files-block #lesson_files_input').send_keys(resource('Document_1.pdf'))
    browser.element('#files-tbody .file-to-speech').click()
    browser.element('.lesson-files-block #lesson_files_input').send_keys(resource('schedule.xlsx'))

    # Create lesson

    browser.element('.lector-name').type('אולגה מסקרפונה')
    time.sleep(2)
    browser.element('.suggestions [data-id="48"]').click()
    browser.element('.add_lecturer').click()

    # Part of lesson
    # part #1
    browser.element('.add-video').click()
    browser.element('.open-video-collapse .lesson-part-toggle').click()
    browser.element('#lesson_part1 .page_video_title').type('Microeconomics lesson 1 - part A')
    browser.element('.lesson_video_file').send_keys(resource('Mathematics.mp4'))
    browser.element('.checkbox-span .summary_to_speech_input').click()
    browser.element('.hide_text_if_there_is_speech_input').click()
    browser.element('#save-lesson').perform(command.js.scroll_into_view)
    browser.element('.vimeo_transcoding_text').with_(timeout=15).should(have.text('Video was uploaded and is '
                                                                                  'being transcoded by '
                                                                                  'vimeo.\nThis may take some '
                                                                                  'time.\nYou can save now and '
                                                                                  'check for image later.'))
    browser.element('#save-lesson').click()
    browser.element('.open-video-collapse .lesson-part-toggle').click()

    # part #2
    browser.element('.add-video').perform(command.js.click)
    time.sleep(1)
    browser.element('.lesson-video:nth-child(2) .lesson-part-toggle').click()
    browser.element('.lesson-video:nth-child(2) .page_video_title').type('Microeconomics Lesson 1 - Part B')
    browser.element('.lesson-video:nth-child(2) .lesson_video_file').send_keys(resource('Mathematics2.mp4'))
    browser.element('#save-lesson').perform(command.js.scroll_into_view)
    browser.element('.lesson-video:nth-child(2) .vimeo_transcoding_text').with_(timeout=15). \
        should(have.text('Video was uploaded and is '
                         'being transcoded by '
                         'vimeo.\nThis may take some '
                         'time.\nYou can save now and '
                         'check for image later.'))
    browser.element('#save-lesson').click()
    browser.element('.lesson-video:nth-child(2) .lesson-part-toggle').click()

#добавить перемещение местами блоки

    # Delete
    browser.element('.lessons-nav-li').click()
    browser.element('[data-name="title"').type('Microeconomics - lesson 1')
    browser.element('.ui-sortable-handle .col').with_(timeout=6).should(have.text('Microeconomics - lesson 1'))
    browser.element('.ui-sortable-handle .delete').click()
    browser.element('.container .btn:nth-child(1)').click()
    browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('Lesson has been deleted'))
