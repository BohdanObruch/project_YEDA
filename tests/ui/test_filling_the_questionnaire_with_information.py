import time
import pytest
import os

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource
from allure import title, tag, step


@tag("Web UI")
@title("Filling in the created questionnaire")
def test_filling_the_questionnaire(setup_browser):
    # browser = setup_browser
    NAME_QUESTIONNAIRE = os.getenv('name_questionnaire')

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the Questionnaires page"):
        browser.element('.elearning-nav-li').click()
        browser.element('.questionnaires-nav-li').click()

    with step("Checking the Questionnaires page display"):
        browser.element('.page-header').with_(timeout=4).should(have.text('Questionnaires'))

    with step(f"Open the created questionnaire - {NAME_QUESTIONNAIRE}"):
        browser.element(f'//*[text() = "{NAME_QUESTIONNAIRE}"]').click()

        with step("Checking the 'Editing Questionnaire' page display"):
            browser.element('.page-header').should(have.text(' Editing Questionnaire'))

        with step("Added Chapters"):
            with step("Added Chapters Title"):
                browser.element('.col-md-9 #edit-chapters').click()
                browser.element('#create-chapter [name="title"]').type('mathematics')
                browser.element('#create-chapter [name="multiplier"]').type('1')
                browser.element('#create-chapter .btn').click()

            with step("Added Categories"):
                browser.element('.create-category [name="new-title"]').type('correct answer')
                browser.element('.create-category .btn').click()

            with step("Added Subcategories"):
                browser.element('.create-subcategory [name="new-title"]').type('higher mathematics')
                browser.element('.create-subcategory .btn').click()
                browser.element('#question_partition_modal .modal-footer .btn').click()

        with step("List of Questionnaire Chapters"):
            with step("Create a New Practice(Question 1)"):
                browser.element('#questionnaire-chapters').with_(timeout=4).should(have.text('List of Questionnaire '
                                                                                             'Chapters'))
                browser.element('#questionnaire-chapters .questionnaire-chapter-create').click()
                browser.element('#questionnaire-chapters .create_new_question').click()

                with step("Added a Question"):
                    browser.element('.col-sm-6:nth-child(1) .jodit-toolbar-button_image .jodit-toolbar-button__button')\
                        .click()
                    browser.element('.jodit-tab [type="file"]').send_keys(resource('questionnaire1.jpeg'))

                with step("Added a Solution explanation"):
                    browser.element('.col-sm-6:nth-child(2) .jodit-toolbar-button_image .jodit-toolbar-button__button')\
                        .click()
                    browser.element('.jodit-tab [type="file"]').send_keys(resource('questionnaire2.jpeg'))

                with step("Added a Tags"):
                    browser.element('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').type('mathematics')\
                        .press_enter()

                with step("Added Difficulty level"):
                    browser.element('#difficulty_level_dropdown .dropdown-toggle').click()
                    browser.element('#difficulty_level_dropdown .dropdown-menu').element('[data-id="1"]').click()

                with step("Selected Chapters"):
                    browser.element('#questions_chapter_dropdown .dropdown-toggle').click()
                    browser.element('#questions_chapter_dropdown .dropdown-menu .dropdown-item').click()

                with step("Selected Category"):
                    browser.element('#questions_category_dropdown .dropdown-toggle').click()
                    browser.element('#questions_category_dropdown .dropdown-menu .dropdown-item').click()

                with step("Selected Subcategory"):
                    browser.element('#questions_sub_category_dropdown .dropdown-toggle').click()
                    browser.element('#questions_sub_category_dropdown .dropdown-menu .dropdown-item').click()

                with step("Added video to answer solution"):
                    browser.element('#video_file').send_keys(resource('Mathematics.mp4'))
                    browser.element('#video #vimeo_transcoding_text').with_(timeout=15)\
                        .should(have.text('Video was uploaded and is being transcoded by vimeo.\nThis may take some '
                                          'time.\nYou can save now and check for image later.'))

                with step("Filling in the answers"):
                    browser.element('.answer .text').type('1')
                    browser.element('.answer:nth-child(2) .text').type('2')
                    browser.element('.answer:nth-child(3) .text').type('3')
                    browser.element('.answer:nth-child(4) .text').type('4')
                    browser.element('.answer:nth-child(1) .question-answers').click()

                with step("Saving a Question and checking that the push notification about saving is displayed"):
                    browser.element('#add-question-footer .btn-primary').click()
                    browser.element('[data-notify="message"]').with_(timeout=4)\
                        .should(have.text('Data has been successfully saved'))

        with step("Added Chapter"):
            with step("Added Chapter Title"):
                browser.element('.col-md-9 #edit-chapters').click()
                browser.element('#create-chapter [name="title"]').type('English')
                browser.element('#create-chapter [name="multiplier"]').clear().type('2')
                browser.element('#create-chapter .btn').click()

            with step("Added Categorie"):
                browser.element('.chapter:nth-child(2) .create-category [name="new-title"]').type('Reading passages')
                browser.element('.chapter:nth-child(2) .create-category .btn').click()
                browser.element('#question_partition_modal .modal-footer .btn').click()

        with step("List of Questionnaire Chapters"):
            with step("Create a New Practice(Question 2)"):
                browser.element('#questionnaire-chapters .create_new_question').click()

                with step("Added a Question"):
                    browser.element('.col-sm-6:nth-child(1) .jodit-toolbar-button_image .jodit-toolbar-button__button')\
                        .click()
                    browser.element('.jodit-tab [type="file"]').send_keys(resource('english.png'))
                    time.sleep(2)

                with step("Added a Tag"):
                    browser.element('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').type('English')\
                        .press_enter()

                with step("Selected Chapter"):
                    browser.element('#questions_chapter_dropdown .dropdown-toggle').click()
                    browser.element('#questions_chapter_dropdown .dropdown-menu li:nth-child(2)').click()

                with step("Selected Category"):
                    browser.element('#questions_category_dropdown .dropdown-toggle').click()
                    browser.element('#questions_category_dropdown .dropdown-menu li:nth-child(2)').click()

                with step("Filling in the answers"):
                    browser.element('.answer .text').type('The method used for testing science students.')
                    browser.element('.answer:nth-child(2) .text').type('The kinds of games that are used in science '
                                                                       'classes.')
                    browser.element('.answer:nth-child(3) .text').type('The way that sciences are taught in high '
                                                                       'school.')
                    browser.element('.answer:nth-child(4) .text').type('The subjects taught in science classes.')
                    browser.element('.answer:nth-child(3) .question-answers').click()
                    browser.element('#add-question-footer .btn-primary').click()

                with step("Saving a Question and checking that the push notification about saving is displayed"):
                    browser.element('[data-notify="message"]').with_(timeout=4).should(have.text('Data has been '
                                                                                                 'successfully saved'))
            with step("Checking the number of created questions"):
                browser.element('.questionnaire-chapter:nth-child(1) .count').with_(timeout=4)\
                    .should(have.text('Questions count - 2'))

        with step("List of Questionnaire Chapters"):
            browser.element('#questionnaire-chapters').with_(timeout=4).should(have.text('List of Questionnaire '
                                                                                         'Chapters'))
            with step("Create a New Practice(Question 3)"):
                browser.element('#questionnaire-chapters .questionnaire-chapter-create').click()
                browser.element('.questionnaire-chapter:nth-child(2) .create_new_question').click()

                with step("Added a Question"):
                    browser.element('.modal-body .col-sm-6:nth-child(1) .jodit-wysiwyg').type('Planets closest to the '
                                                                                              'Sun (called '
                                                                                              'terrestrial planets)')

                with step("Added a Tag"):
                    browser.element('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').type('Solar System')\
                        .press_enter()

                with step("Added Difficulty level"):
                    browser.element('#difficulty_level_dropdown .dropdown-toggle').click()
                    browser.element('#difficulty_level_dropdown .dropdown-menu').element('[data-id="1"]').click()

                with step("Changing the question type"):
                    browser.element('#typeDropdownMenuButton').click()
                    browser.element('.dropdown-menu [data-type="checkbox"]').click()

                with step("Filling in the answers"):
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

                with step("Indicating the correct answer option"):
                    browser.element('.answer:nth-child(2) .question-answers').click()
                    browser.element('.answer:nth-child(4) .question-answers').click()
                    browser.element('.answer:nth-child(6) .question-answers').click()
                    browser.element('.answer:nth-child(8) .question-answers').click()
                    browser.element('#add-question-footer .btn-primary').click()

                with step("Saving a Question and checking that the push notification about saving is displayed"):
                    browser.element('[data-notify="message"]').with_(timeout=4).should(have.text('Data has been '
                                                                                                 'successfully saved'))

                with step("Checking the number of created questions"):
                    browser.element('.questionnaire-chapter:nth-child(2) .count').with_(timeout=4)\
                        .should(have.text('Questions count - 1'))

        with step("List of Questionnaire Chapters"):
            browser.element('#questionnaire-chapters').with_(timeout=4).should(have.text('List of Questionnaire Chapters'))

            with step("Create Questionnaire Chapter"):
                browser.element('#questionnaire-chapters .questionnaire-chapter-create').click()

                with step("Added a Question"):
                    browser.element('.questionnaire-chapter:nth-child(3) .add-question').click()

                    with step("importing questions from other questionnaires"):
                        browser.element('#search-questions-list [data-id="76"]').click()
                        browser.element('#search-questions-list [data-id="78"]').click()
                        browser.element('#search-questions-list [data-id="62"]').click()
                        browser.element('.modal-footer #sq_save').click()

                with step("Checking the number of created questions"):
                    browser.element('.questionnaire-chapter:nth-child(3) .count').with_(timeout=4)\
                        .should(have.text('Questions count - 3'))

        with step("Add title Questionnaire Chapters"):
            with step("Add title Questionnaire Chapters #1"):
                browser.element('.list .questionnaire-chapter:nth-child(1) .edit').click()
                browser.element('.list .questionnaire-chapter:nth-child(1) .chapter-name')\
                    .type('Questionnaire Chapter #1')
                browser.element('.list .questionnaire-chapter:nth-child(1) .save').click()

            with step("Add title Questionnaire Chapters #2"):
                browser.element('.list .questionnaire-chapter:nth-child(2) .edit').click()
                browser.element('.list .questionnaire-chapter:nth-child(2) .chapter-name')\
                    .type('Questionnaire Chapter #2')
                browser.element('.list .questionnaire-chapter:nth-child(2) .save').click()

            with step("Add title Questionnaire Chapters #3"):
                browser.element('.list .questionnaire-chapter:nth-child(3) .edit').click()
                browser.element('.list .questionnaire-chapter:nth-child(3) .chapter-name')\
                    .type('Questionnaire Chapter #3')
                browser.element('.list .questionnaire-chapter:nth-child(3) .save').click()

        with step("Edit Chapters"):
            with step("Delete Chapters #1"):
                browser.element('.col-md-9 #edit-chapters').click()
                browser.element('#chapters .chapter .delete').click()
                browser.element('.container .btn:nth-child(1)').click()

            with step("Delete Chapters #2"):
                browser.element('#chapters .chapter .delete').click()
                browser.element('.container .btn:nth-child(1)').click()
                browser.element('#question_partition_modal .modal-footer .btn').click()

    with step("Deleting a created questionnaires"):
        with step("Go to the page with all the questionnaires"):
            browser.element('.questionnaires-nav-li').click()
            browser.element('.page-header').with_(timeout=4).should(have.text('Questionnaires'))

        with step("Search for a created questionnaire and delete it"):
            browser.element('.filter #search_text').type(NAME_QUESTIONNAIRE).press_enter()
            browser.element('#sortable .questionnaire-link').with_(timeout=4).should(have.text(NAME_QUESTIONNAIRE))
            browser.element('#sortable .questionnaire-delete').click()
            browser.element('.jconfirm-box .btn:nth-child(1)').click()

        with step("Display a push message about successful removal of the questionnaire"):
            browser.element('[data-notify="message"]').with_(timeout=5).should(have.text('questionnaire has been '
                                                                                         'deleted'))
