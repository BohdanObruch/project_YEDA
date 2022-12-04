from allure import title, tag, step
from diploma_project_tests.model.authorization import authorization_on_admin_panel
from diploma_project_tests.helpers import app
from diploma_project_tests.data.data import *


@tag("Web UI")
@title("Creating survey")
def test_create_survey(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Going to the Surveys page"):
        app.survey_page.open_surveys_page()

    with step("Checking the 'Surveys' page display"):
        app.survey_page.checking_the_display_of_the_surveys_page('Surveys')

    with step("Creating survey"):
        app.survey_page.creat_survey()

        with step("Checking the 'Adding Survey' page display"):
            app.survey_page.checking_title_survey_page('Adding Survey')

        with step("General block"):
            with step("Filling in the title"):
                app.survey_page.add_title()

            with step("Filling in the opening text"):
                app.survey_page.add_opening_text()

            with step("Filling in the final text"):
                app.survey_page.add_final_text(Survey.final_text)

            with step("Changing the status to active to display on the site"):
                app.survey_page.change_status()

        with step("Submit the form"):
            app.survey_page.submit_form()

        with step("Checking the 'Adding Survey' page display"):
            app.survey_page.checking_title_survey_page('Editing Survey')


@tag("Web UI")
@title("Filling in the survey information")
def test_filling_survey(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Going to the Surveys page"):
        app.survey_page.open_surveys_page()

    with step("Open created survey"):
        app.survey_page.open_created_survey()

    with step("Questions block"):
        with step("Checking the 'Editing Survey' page display"):
            app.survey_page.checking_editing_survey_page('Editing Survey')

        with step("Checking the display of the 'Questions' tab and opening it"):
            app.survey_page.checking_questions_tab_open('Questions')

        with step("Adding questions"):
            with step("Adding a question of type - 'Text'"):
                app.survey_page.add_first_questions_type_text(Survey.message_notification, Survey.first_question_type)

                with step("Adding a question"):
                    app.survey_page.add_first_question_content(Survey.content_first_question)

                with step("Specifying the number of characters to answer"):
                    app.survey_page.add_number_of_characters_to_answer(Survey.number_of_characters)

                with step("Indication as a mandatory question and the next button"):
                    app.survey_page.add_mandatory_first_question_and_add_the_next_button()

            with step("Adding a question of type - 'Paragraph'"):
                app.survey_page.add_second_questions_type_paragraph(Survey.message_notification,
                                                                    Survey.second_question_type)

                with step("Adding a question"):
                    app.survey_page.add_second_question_content(Survey.content_second_question)

            with step("Adding a question of type - 'Single choice'"):
                app.survey_page.add_third_questions_type_single_choice(Survey.message_notification,
                                                                       Survey.third_question_type)

                with step("Adding a question"):
                    app.survey_page.add_third_question_content(Survey.content_third_question)

                    with step("Adding answers to question"):
                        app.survey_page.add_answers_to_third_question(Survey.first_answer, Survey.second_answer,
                                                                      Survey.third_answer)

            with step("Adding a question of type - 'Multiple choice'"):
                app.survey_page.add_fourth_questions_type_multiple_choice(Survey.fourth_question_type)

                with step("Adding a question"):
                    app.survey_page.add_fourth_question_content(Survey.content_fourth_question)

                    with step("Adding answers to question"):
                        app.survey_page.add_answers_to_fourth_question(Survey.first_answer_option,
                                                                       Survey.second_answer_option,
                                                                       Survey.third_answer_option,
                                                                       Survey.fourth_answer_option,
                                                                       Survey.fifth_answer_option,
                                                                       Survey.sixth_answer_option,
                                                                       Survey.seventh_answer_option)

            with step("Adding a question of type - 'Select from list'"):
                app.survey_page.add_fifth_questions_type_select_from_list(Survey.fifth_question_type)

                with step("Adding a question"):
                    app.survey_page.add_fifth_question_content(Survey.content_fifth_question)

                    with step("Adding answers to question"):
                        app.survey_page.add_answers_to_fifth_question(Survey.first_answer_variant,
                                                                      Survey.second_answer_variant,
                                                                      Survey.third_answer_variant)

            with step("Adding a question of type - 'Rating'"):
                app.survey_page.add_sixth_questions_type_rating(Survey.sixth_question_type)

                with step("Adding a question"):
                    app.survey_page.add_sixth_question_content(Survey.content_sixth_question)

                    with step("Adding answers to question"):
                        app.survey_page.add_answers_to_sixth_question(Survey.first_answer_version,
                                                                      Survey.second_answer_version)

            with step("Checking question type and sequence number"):
                app.survey_page.checking_question_type_and_sequence_number('Rating . Question 6')


@tag("Web UI")
@title("Duplication of the question")
def test_duplication_of_the_question(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Going to the Surveys page"):
        app.survey_page.open_surveys_page()

    with step("Open created survey"):
        app.survey_page.open_created_survey()

    with step("Question replication"):
        app.survey_page.adding_question_replication(Survey.seventh_question_type)

    with step("Checking the display of a push message about the question has been duplicated"):
        app.survey_page.checking_the_display_push_message('question has been duplicated')


@tag("Web UI")
@title("Import questions from another surveys")
def test_import_questions(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Going to the Surveys page"):
        app.survey_page.open_surveys_page()

    with step("Open created survey"):
        app.survey_page.open_created_survey()

    with step("Import questions from another survey"):
        app.survey_page.import_first_questions_from_another_survey(Survey.import_question_text)

        with step("Choosing a first survey with questions"):
            app.survey_page.search_and_choosing_first_a_survey(Survey.name_first_survey)

    with step("Import questions from another survey"):
        app.survey_page.import_second_questions_from_another_survey(Survey.import_question_text)

        with step("Choosing a second survey with questions"):
            app.survey_page.search_and_choosing_second_a_survey(Survey.name_second_survey)

        with step("Checking the display of a push message about the import of questions"):
            app.survey_page.checking_the_display_push_message('questions were imported')


@tag("Web UI")
@title("Deleting question from survey")
def test_deleting_question(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Going to the Surveys page"):
        app.survey_page.open_surveys_page()

    with step("Open created survey"):
        app.survey_page.open_created_survey()

    with step("Delete one question"):
        app.survey_page.delete_one_question()

    with step("Check the display of a push message about the removal of the question"):
        app.survey_page.checking_the_display_push_message('question has been deleted')
