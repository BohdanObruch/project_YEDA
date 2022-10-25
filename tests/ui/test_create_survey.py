import time
import lorem

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource
from allure import title, tag, step

title_survey = lorem.sentence()
content_survey = lorem.paragraph()


@tag("Web UI")
@title("Creating a survey and filling it with information")
def test_add_survey(setup_browser):
    # browser = setup_browser

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the Surveys page"):
        browser.element('.elearning-nav-li').click()
        browser.element('.surveys-nav-li').click()

    with step("Checking the 'Surveys' page display"):
        browser.element('.page-header').with_(timeout=4).should(have.text('Surveys'))

    with step("Creating survey"):
        browser.element('.panel-heading .btn').click()

        with step("Checking the 'Adding Survey' page display"):
            browser.element('.page-header').with_(timeout=4).should(have.text('Adding Survey'))

        with step("General block"):
            with step("Filling in the title"):
                browser.element('#survey-title').type(title_survey)

            with step("Filling in the opening text"):
                browser.element('#store_survey_form div:nth-child(4) .jodit-wysiwyg').type(content_survey)

            with step("Filling in the final text"):
                browser.element('#store_survey_form div:nth-child(5) .jodit-wysiwyg').type('Thanks!')

            with step("Changing the status to active to display on the site"):
                browser.element('#is_active').click()

        with step("Submit the form"):
            browser.element('#store_survey_form .btn-primary').click()

    with step("Questions block"):
        with step("Checking the 'Editing Survey' page display"):
            browser.element('.page-header').with_(timeout=4).should(have.text('Editing Survey'))

        with step("Checking the display of the 'Questions' tab and opening it"):
            browser.element('.panel:nth-child(2) .panel-heading .panel-title').should(have.text('Questions'))
            browser.element('.panel:nth-child(2) .panel-heading .open-panel').click()

        with step("Adding questions"):
            browser.element('#questions-panel #survey-new-question').click()

            with step("Adding a question of type - 'Text'"):
                browser.element('[data-notify="message"]').with_(timeout=3) \
                    .should(have.text('question data has been saved'))
                browser.element('.survey-question:nth-child(1) .panel-title').should(have.text('Text. Question 1'))

                with step("Adding a question"):
                    browser.element('#survey-questions .jodit-wysiwyg').type('Express your opinion about the lesson.')

                with step("Specifying the number of characters to answer"):
                    browser.element('#survey-question-number-of-characters').clear().type('100')

                with step("Indication as a mandatory question and the next button"):
                    browser.element('#survey-questions .survey-question-is-mandatory').click()
                    browser.element('#survey-questions .survey-question-do-show-next').click()

            with step("Adding a question of type - 'Paragraph'"):
                browser.element('.panel-body #survey-new-question-type').click()
                browser.element('#survey-new-question-type [value="paragraph"]').click()
                browser.element('#questions-panel #survey-new-question').click()
                browser.element('.survey-question:nth-child(2) .panel-title').should(have.text('Paragraph. Question 2'))
                browser.element('[data-notify="message"]').with_(timeout=3) \
                    .should(have.text('question data has been saved'))

                with step("Adding a question"):
                    browser.element('#survey-questions .survey-question:nth-child(2) .jodit-wysiwyg') \
                        .type('Did you study all the '
                              'lessons in the section '
                              'and still have questions? '
                              'If so, please list them.')

                with step("Indication as a mandatory question and the next button"):
                    browser.element('.survey-question:nth-child(2) .survey-question-is-mandatory').click()
                    browser.element('.survey-question:nth-child(2) .survey-question-do-show-next').click()

            with step("Adding a question of type - 'Single choice'"):
                browser.element('.panel-body #survey-new-question-type').click()
                browser.element('#survey-new-question-type [value="single-choice"]').click()
                browser.element('#questions-panel #survey-new-question').click()
                browser.element('.survey-question:nth-child(3) .panel-title').should(have.text('Single choice. '
                                                                                               'Question 3'))
                browser.element('[data-notify="message"]').with_(timeout=3).should(have.text('question data has been '
                                                                                             'saved'))

                with step("Adding a question"):
                    browser.element('#survey-questions .survey-question:nth-child(3) .jodit-wysiwyg') \
                        .type('Was the lecturer clear?')

                    with step("Adding answers to question"):
                        browser.element('.survey-question:nth-child(3) .input-group:nth-child(1) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(3) .input-group:nth-child(1) '
                                        '.survey-question-choice').type('Very well')
                        browser.element('.survey-question:nth-child(3) .input-group:nth-child(2) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(3) .input-group:nth-child(2) '
                                        '.survey-question-choice').type('Not so')
                        browser.element('.survey-question:nth-child(3) .input-group:nth-child(3) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(3) .input-group:nth-child(3) '
                                        '.survey-question-choice').type('I only understood some of the things')

                with step("Indication as a mandatory question and the next button"):
                    browser.element('.survey-question:nth-child(3) .survey-question-is-mandatory').click()
                    browser.element('.survey-question:nth-child(3) .survey-question-do-show-next').click()

            with step("Adding a question of type - 'Multiple choice'"):
                browser.element('.panel-body #survey-new-question-type').click()
                browser.element('#survey-new-question-type [value="multiple-choice"]').click()
                browser.element('#questions-panel #survey-new-question').click()
                browser.element('.survey-question:nth-child(4) .panel-title').should(have.text('Multiple choice. '
                                                                                               'Question 4'))
                browser.element('[data-notify="message"]').with_(timeout=3).should(have.text('question data has been '
                                                                                             'saved'))

                with step("Adding a question"):
                    browser.element('.survey-question:nth-child(4) .jodit-wysiwyg').type('What device are you '
                                                                                         'accessing the system '
                                                                                         'from right now?')

                    with step("Adding answers to question"):
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(1) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(1) '
                                        '.survey-question-choice').type('IOS tablet')
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(2) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(2) '
                                        '.survey-question-choice').type('Android tablet')
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(3) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(3) '
                                        '.survey-question-choice').type('Android phone')
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(4) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(4) '
                                        '.survey-question-choice').type('IOS phone')
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(5) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(5) '
                                        '.survey-question-choice').type('Windows phone')
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(6) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(6) '
                                        '.survey-question-choice').type('Windows computer')
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(7) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(4) .input-group:nth-child(7) '
                                        '.survey-question-choice').type('Mac computer')

                with step("Indication as a mandatory question and the next button"):
                    browser.element('.survey-question:nth-child(4) .survey-question-is-mandatory').click()
                    browser.element('.survey-question:nth-child(4) .survey-question-do-show-next').click()

            with step("Adding a question of type - 'Select from list'"):
                browser.element('.panel-body #survey-new-question-type').click()
                browser.element('#survey-new-question-type [value="select-from-list"]').click()
                browser.element('#questions-panel #survey-new-question').click()
                browser.element('.survey-question:nth-child(5) .panel-title').should(have.text('Select from list. '
                                                                                               'Question 5'))

                with step("Adding a question"):
                    browser.element('.survey-question:nth-child(5) .jodit-wysiwyg').type('Do you feel that you master '
                                                                                         'the material '
                                                                                         'studied?')

                    with step("Adding answers to question"):
                        browser.element('.survey-question:nth-child(5) .input-group:nth-child(1) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(5) .input-group:nth-child(1) '
                                        '.survey-question-choice').type('Very well')
                        browser.element('.survey-question:nth-child(5) .input-group:nth-child(2) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(5) .input-group:nth-child(2) '
                                        '.survey-question-choice').type('There is something to refine')
                        browser.element('.survey-question:nth-child(5) .input-group:nth-child(3) '
                                        '.survey-question-choice').click()
                        time.sleep(0.5)
                        browser.element('.survey-question:nth-child(5) .input-group:nth-child(3) '
                                        '.survey-question-choice').type('Not so')

                    with step("Indication as a mandatory question and the next button"):
                        browser.element('.survey-question:nth-child(5) .survey-question-is-mandatory').click()
                        browser.element('.survey-question:nth-child(5) .survey-question-do-show-next').click()

            with step("Adding a question of type - 'Rating'"):
                browser.element('.panel-body #survey-new-question-type').click()
                browser.element('#survey-new-question-type [value="rating"]').click()
                browser.element('#questions-panel #survey-new-question').click()
                browser.element('.survey-question:nth-child(6) .panel-title').should(have.text('Rating. Question 6'))

                with step("Adding a question"):
                    browser.element('.survey-question:nth-child(6) .jodit-wysiwyg').type('Please rate from 1 to 5 how '
                                                                                         'convenient and '
                                                                                         'intuitive the system is for '
                                                                                         'the student to '
                                                                                         'use.')

                    with step("Adding answers to question"):
                        browser.element('.survey-question:nth-child(6) .survey-question-from-input')\
                            .type("Not comfortable at all, it's hard to understand the order of the study process")
                        browser.element('.survey-question:nth-child(6) .survey-question-to-input')\
                            .type('The system is very understandable and intuitive to use')

                    with step("Indication as a mandatory question and the next button"):
                        browser.element('.survey-question:nth-child(6) .survey-question-is-mandatory').click()
                        browser.element('.survey-question:nth-child(6) .survey-question-do-show-next').click()

        with step("Question replication"):
            browser.element('.survey-question:nth-child(6) .survey-question-copy').click()
            browser.element('.survey-question:nth-child(7) .panel-title').should(have.text('Rating. Question 7'))

        with step("Import questions from another survey"):
            browser.element('.panel-body #survey-import-questions-modal-open').click()
            browser.element('[for="survey-import-title"]').with_(timeout=3)\
                .should(have.text('Choose survey to import questions'))

            with step("Choosing a survey with questions"):
                browser.element('#survey-import-modal #survey-import-questions-input').click()
                browser.element('[data-id="29"]').click()
                browser.element('#survey-import-modal #survey-import-questions').click()

        with step("Import questions from another survey"):
            browser.element('.panel-body #survey-import-questions-modal-open').click()
            browser.element('[for="survey-import-title"]').with_(timeout=3).should(
                    have.text('Choose survey to import questions'))

            with step("Choosing a survey with questions"):
                browser.element('#survey-import-modal #survey-import-questions-input').click().clear().type(
                        'המלצות ומשובים על הקורס')
                browser.element('[data-id="99"]').click()
                browser.element('#survey-import-modal #survey-import-questions').click()

        with step("Delete one question"):
            browser.element('.survey-question:nth-child(7) .panel-heading .fa-trash').click()
            browser.element('.container .btn-default:nth-child(1)').click()
