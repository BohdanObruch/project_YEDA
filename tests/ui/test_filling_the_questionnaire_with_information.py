import time

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource
from tests.ui.test_create_questionnaire import name_questionnaire


def test_filling_the_questionnaire(setup_browser):
    # browser = setup_browser

    authorization_on_admin_panel()

    browser.element('.elearning-nav-li').click()
    browser.element('.questionnaires-nav-li').click()

    browser.element('.page-header').with_(timeout=4).should(have.text('Questionnaires'))

    browser.element(f'//*[text() = "{name_questionnaire}"]').click()  # The provider - practice before the course

    browser.element('.page-header').should(have.text(' Editing Questionnaire'))

    # chapters
    browser.element('.col-md-9 #edit-chapters').click()
    browser.element('#create-chapter [name="title"]').type('mathematics')
    browser.element('#create-chapter [name="multiplier"]').type('1')
    browser.element('#create-chapter .btn').click()

    browser.element('.create-category [name="new-title"]').type('correct answer')
    browser.element('.create-category .btn').click()

    browser.element('.create-subcategory [name="new-title"]').type('higher mathematics')
    browser.element('.create-subcategory .btn').click()

    browser.element('#question_partition_modal .modal-footer .btn').click()

    # add question1

    browser.element('#questionnaire-chapters').with_(timeout=4).should(have.text('List of Questionnaire Chapters'))
    browser.element('#questionnaire-chapters .questionnaire-chapter-create').click()
    browser.element('#questionnaire-chapters .create_new_question').click()

    browser.element('.col-sm-6:nth-child(1) .jodit-toolbar-button_image .jodit-toolbar-button__button').click()
    browser.element('.jodit-tab [type="file"]').send_keys(resource('questionnaire1.jpeg'))
    browser.element('.col-sm-6:nth-child(2) .jodit-toolbar-button_image .jodit-toolbar-button__button').click()
    browser.element('.jodit-tab [type="file"]').send_keys(resource('questionnaire2.jpeg'))

    browser.element('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').type('mathematics').press_enter()

    browser.element('#difficulty_level_dropdown .dropdown-toggle').click()
    browser.element('#difficulty_level_dropdown .dropdown-menu').element('[data-id="1"]').click()

    browser.element('#questions_chapter_dropdown .dropdown-toggle').click()
    browser.element('#questions_chapter_dropdown .dropdown-menu .dropdown-item').click()

    browser.element('#questions_category_dropdown .dropdown-toggle').click()
    browser.element('#questions_category_dropdown .dropdown-menu .dropdown-item').click()

    browser.element('#questions_sub_category_dropdown .dropdown-toggle').click()
    browser.element('#questions_sub_category_dropdown .dropdown-menu .dropdown-item').click()

    # answer video
    browser.element('#video_file').send_keys(resource('Mathematics.mp4'))
    browser.element('#video #vimeo_transcoding_text').with_(timeout=15).should(have.text('Video was uploaded and is '
                                                                                         'being transcoded by '
                                                                                         'vimeo.\nThis may take some '
                                                                                         'time.\nYou can save now and '
                                                                                         'check for image later.'))

    # Answer
    browser.element('.answer .text').type('1')
    browser.element('.answer:nth-child(2) .text').type('2')
    browser.element('.answer:nth-child(3) .text').type('3')
    browser.element('.answer:nth-child(4) .text').type('4')
    browser.element('.answer:nth-child(1) .question-answers').click()
    browser.element('#add-question-footer .btn-primary').click()

    browser.element('[data-notify="message"]').with_(timeout=4).should(have.text('Data has been successfully saved'))

    # chapters
    browser.element('.col-md-9 #edit-chapters').click()
    browser.element('#create-chapter [name="title"]').type('English')
    browser.element('#create-chapter [name="multiplier"]').clear().type('2')
    browser.element('#create-chapter .btn').click()

    browser.element('.chapter:nth-child(2) .create-category [name="new-title"]').type('Reading passages')
    browser.element('.chapter:nth-child(2) .create-category .btn').click()

    browser.element('#question_partition_modal .modal-footer .btn').click()

    # add question2

    browser.element('#questionnaire-chapters .create_new_question').click()

    browser.element('.col-sm-6:nth-child(1) .jodit-toolbar-button_image .jodit-toolbar-button__button').click()
    browser.element('.jodit-tab [type="file"]').send_keys(resource('english.png'))
    time.sleep(2)

    # Chapters in question2
    browser.element('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').type('English').press_enter()

    browser.element('#questions_chapter_dropdown .dropdown-toggle').click()
    browser.element('#questions_chapter_dropdown .dropdown-menu li:nth-child(2)').click()  # english

    browser.element('#questions_category_dropdown .dropdown-toggle').click()
    browser.element('#questions_category_dropdown .dropdown-menu li:nth-child(2)').click()  # Reading passages

    # Answer
    browser.element('.answer .text').type('The method used for testing science students.')
    browser.element('.answer:nth-child(2) .text').type('The kinds of games that are used in science classes.')
    browser.element('.answer:nth-child(3) .text').type('The way that sciences are taught in high school.')
    browser.element('.answer:nth-child(4) .text').type('The subjects taught in science classes.')
    browser.element('.answer:nth-child(3) .question-answers').click()
    browser.element('#add-question-footer .btn-primary').click()

    browser.element('[data-notify="message"]').with_(timeout=4).should(have.text('Data has been successfully saved'))

    browser.element('.questionnaire-chapter:nth-child(1) .count').with_(timeout=4).should(have.text('Questions count '
                                                                                                    '- 2'))

    # add question3

    browser.element('#questionnaire-chapters').with_(timeout=4).should(have.text('List of Questionnaire Chapters'))
    browser.element('#questionnaire-chapters .questionnaire-chapter-create').click()
    browser.element('.questionnaire-chapter:nth-child(2) .create_new_question').click()

    browser.element('.modal-body .col-sm-6:nth-child(1) .jodit-wysiwyg').type('Planets closest to the Sun (called '
                                                                              'terrestrial planets)')

    # Chapters in question3
    browser.element('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').type('Solar System').press_enter()
    #
    browser.element('#difficulty_level_dropdown .dropdown-toggle').click()
    browser.element('#difficulty_level_dropdown .dropdown-menu').element('[data-id="1"]').click()

    # Type
    browser.element('#typeDropdownMenuButton').click()
    browser.element('.dropdown-menu [data-type="checkbox"]').click()

    # Answer
    browser.element('.answer .text').type('Mercury')
    browser.element('.answer:nth-child(2) .text').type('Jupiter')
    browser.element('.answer:nth-child(3) .text').type('Venus')
    browser.element('.answer:nth-child(4) .text').type('Uranus')
    browser.element('.answer:nth-child(5) [type="text"]').perform(command.js.scroll_into_view)
    browser.element('.answer:nth-child(5) .text').type('Earth').click()
    browser.element('.answer:nth-child(6) .text').type('Neptune').click()
    browser.element('.answer:nth-child(7) .text').type('Mars').click()
    browser.element('.answer:nth-child(8) .text').type('Saturn').click()
    browser.element('.answer:nth-child(8) .text').perform(command.js.scroll_into_view).click()

    browser.element('.answer:nth-child(2) .question-answers').click()
    browser.element('.answer:nth-child(4) .question-answers').click()
    browser.element('.answer:nth-child(6) .question-answers').click()
    browser.element('.answer:nth-child(8) .question-answers').click()
    browser.element('#add-question-footer .btn-primary').click()

    browser.element('[data-notify="message"]').with_(timeout=4).should(have.text('Data has been successfully saved'))

    browser.element('.questionnaire-chapter:nth-child(2) .count').with_(timeout=4).should(have.text('Questions count '
                                                                                                    '- 1'))

    # add question 4,5,6
    browser.element('#questionnaire-chapters').with_(timeout=4).should(have.text('List of Questionnaire Chapters'))
    browser.element('#questionnaire-chapters .questionnaire-chapter-create').click()

    browser.element('.questionnaire-chapter:nth-child(3) .add-question').click()
    browser.element('#search-questions-list [data-id="76"]').click()
    browser.element('#search-questions-list [data-id="78"]').click()
    browser.element('#search-questions-list [data-id="62"]').click()
    browser.element('.modal-footer #sq_save').click()
    browser.element('.questionnaire-chapter:nth-child(3) .count').with_(timeout=4).should(have.text('Questions count '
                                                                                                    '- 3'))
    # Add title Questionnaire Chapters
    browser.element('.list .questionnaire-chapter:nth-child(1) .edit').click()
    browser.element('.list .questionnaire-chapter:nth-child(1) .chapter-name').type('Questionnaire Chapter #1')
    browser.element('.list .questionnaire-chapter:nth-child(1) .save').click()

    browser.element('.list .questionnaire-chapter:nth-child(2) .edit').click()
    browser.element('.list .questionnaire-chapter:nth-child(2) .chapter-name').type('Questionnaire Chapter #2')
    browser.element('.list .questionnaire-chapter:nth-child(2) .save').click()

    browser.element('.list .questionnaire-chapter:nth-child(3) .edit').click()
    browser.element('.list .questionnaire-chapter:nth-child(3) .chapter-name').type('Questionnaire Chapter #3')
    browser.element('.list .questionnaire-chapter:nth-child(3) .save').click()

    # Delete Chapters
    browser.element('.col-md-9 #edit-chapters').click()
    browser.element('#chapters .chapter .delete').click()
    browser.element('.container .btn:nth-child(1)').click()

    browser.element('#chapters .chapter .delete').click()
    browser.element('.container .btn:nth-child(1)').click()

    browser.element('#question_partition_modal .modal-footer .btn').click()


    # Delete
    browser.element('.questionnaires-nav-li').click()
    browser.element('.page-header').with_(timeout=4).should(have.text('Questionnaires'))
    browser.element('.filter #search_text').type(f'{name_questionnaire}').press_enter()
    browser.element('#sortable .questionnaire-link').with_(timeout=4).should(have.text(f'{name_questionnaire}'))

    browser.element('#sortable .questionnaire-delete').click()
    browser.element('.jconfirm-box .btn:nth-child(1)').click()
    browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('questionnaire has been deleted'))

