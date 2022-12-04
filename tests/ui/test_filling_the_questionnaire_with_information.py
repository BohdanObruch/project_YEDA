from diploma_project_tests.model.authorization import authorization_on_admin_panel
from allure import title, tag, step
from diploma_project_tests.helpers import app
from diploma_project_tests.data.data import *


@tag("Web UI")
@title("Filling in the created questionnaire")
def test_filling_the_questionnaire(setup_browser):

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the Questionnaires page"):
        app.filling_questionnaire.open_questionnaires_page()

    with step("Checking the Questionnaires page display"):
        app.filling_questionnaire.checking_questionnaires_page('Questionnaires')

    with step("Open the created questionnaire"):
        app.filling_questionnaire.open_create_questionnaire()

        with step("Checking the 'Editing Questionnaire' page display"):
            app.filling_questionnaire.checking_editing_questionnaire_page('Editing Questionnaire')

        with step("Added Chapters"):
            with step("Added Chapters Title"):
                app.filling_questionnaire.add_first_chapters_title(Questionnaire.first_title_chapters,
                                                                   Questionnaire.first_multiplier)

            with step("Added Category"):
                app.filling_questionnaire.add_first_categories(Questionnaire.first_categories)

            with step("Added Subcategories"):
                app.filling_questionnaire.add_first_subcategories(Questionnaire.subcategories)

        with step("List of Questionnaire Chapters"):
            with step("Create a New Practice(Question 1)"):
                app.filling_questionnaire.create_new_practice_first_question('List of Questionnaire Chapters')

                with step("Added a Question"):
                    app.filling_questionnaire.add_first_question(Questionnaire.first_resource)

                with step("Added a Solution explanation"):
                    app.filling_questionnaire.add_solution_explanation(Questionnaire.second_resource)

                with step("Added a Tags"):
                    app.filling_questionnaire.add_first_tag(Questionnaire.name_first_tag)

                with step("Added Difficulty level"):
                    app.filling_questionnaire.add_difficulty_level_one()

                with step("Selected Chapters"):
                    app.filling_questionnaire.selected_first_chapters()

                with step("Selected Category"):
                    app.filling_questionnaire.selected_first_category()

                with step("Selected Subcategory"):
                    app.filling_questionnaire.selected_first_subcategory()

                with step("Added video to answer solution"):
                    app.filling_questionnaire.add_video_to_answer_solution(Questionnaire.third_resource,
                                                                           Questionnaire.text_video_transcoding)

                with step("Filling in the answers"):
                    app.filling_questionnaire.add_first_answer(Questionnaire.answer_first, Questionnaire.answer_second,
                                                               Questionnaire.answer_third, Questionnaire.answer_fourth)

                with step("Saving a Question and checking that the push notification is displayed"):
                    app.filling_questionnaire.push_message_about_saving_first_question('Data has been successfully '
                                                                                       'saved')

        with step("Added Chapter"):
            with step("Added Chapter Title"):
                app.filling_questionnaire.add_second_chapters_title(Questionnaire.second_title_chapters,
                                                                    Questionnaire.second_multiplier)

            with step("Added Category"):
                app.filling_questionnaire.add_second_categories(Questionnaire.second_categories)

        with step("List of Questionnaire Chapters"):
            with step("Create a New Practice(Question 2)"):
                app.filling_questionnaire.create_new_practice_second_question()

                with step("Added a Question"):
                    app.filling_questionnaire.add_second_question(Questionnaire.fourth_resource)

                with step("Added a Tag"):
                    app.filling_questionnaire.add_second_tag(Questionnaire.name_second_tag)

                with step("Selected Chapter"):
                    app.filling_questionnaire.selected_second_chapters()

                with step("Selected Category"):
                    app.filling_questionnaire.selected_second_category()

                with step("Filling in the answers"):
                    app.filling_questionnaire.add_second_answer(Questionnaire.first_answer, Questionnaire.second_answer,
                                                                Questionnaire.third_answer, Questionnaire.fourth_answer)

                with step("Saving a Question and checking that the push notification about saving is displayed"):
                    app.filling_questionnaire.push_message_about_saving_second_question('Data has been successfully '
                                                                                        'saved')

            with step("Checking the number of created questions"):
                app.filling_questionnaire.checking_the_number_of_created_questions_first_block('Questions count - 2')

        with step("List of Questionnaire Chapters"):
            with step("Create a New Practice(Question 3)"):
                app.filling_questionnaire.create_new_practice_third_question('List of Questionnaire Chapters')

                with step("Added a Question"):
                    app.filling_questionnaire.add_third_question(Questionnaire.third_question)

                with step("Added a Tag"):
                    app.filling_questionnaire.add_third_tag(Questionnaire.name_third_tag)

                with step("Added Difficulty level"):
                    app.filling_questionnaire.add_difficulty_level_second()

                with step("Changing the question type"):
                    app.filling_questionnaire.changing_the_question_type()

                with step("Filling in the answers"):
                    app.filling_questionnaire.add_third_answer(Questionnaire.first_answer_third_question,
                                                               Questionnaire.second_answer_third_question,
                                                               Questionnaire.third_answer_third_question,
                                                               Questionnaire.fourth_answer_third_question,
                                                               Questionnaire.fifth_answer_third_question,
                                                               Questionnaire.sixth_answer_third_question,
                                                               Questionnaire.seventh_answer_third_question,
                                                               Questionnaire.eighth_answer_third_question)

                with step("Indicating the correct answer option"):
                    app.filling_questionnaire.indicating_the_correct_answer()

                with step("Saving a Question and checking that the push notification about saving is displayed"):
                    app.filling_questionnaire.push_message_about_saving_third_question('Data has been '
                                                                                       'successfully saved')

                with step("Checking the number of created questions"):
                    app.filling_questionnaire.checking_the_number_of_created_questions_second_block('Questions count '
                                                                                                    '- 1')

        with step("List of Questionnaire Chapters"):
            with step("Create Questionnaire Chapter"):
                with step("Added a Question"):
                    app.filling_questionnaire.create_new_practice_fourth_question('List of Questionnaire Chapters')

                    with step("importing questions from other questionnaires"):
                        app.filling_questionnaire.importing_questions_from_other_questionnaires()

                with step("Checking the number of created questions"):
                    app.filling_questionnaire.checking_the_number_of_created_questions_third_block('Questions count '
                                                                                                   '- 3')

        with step("Add title Questionnaire Chapters"):
            with step("Add title Questionnaire Chapters #1"):
                app.filling_questionnaire.add_first_title_questionnaire_chapters(
                    Questionnaire.first_questionnaire_title)

            with step("Add title Questionnaire Chapters #2"):
                app.filling_questionnaire.add_second_title_questionnaire_chapters(
                    Questionnaire.second_questionnaire_title)

            with step("Add title Questionnaire Chapters #3"):
                app.filling_questionnaire.add_third_title_questionnaire_chapters(
                    Questionnaire.third_questionnaire_title)

        with step("Edit Chapters"):
            with step("Delete Chapters #1"):
                app.filling_questionnaire.delete_first_chapters()

            with step("Delete Chapters #2"):
                app.filling_questionnaire.delete_second_chapters()

@tag("Web UI")
@title("Filling in the created questionnaire")
def test_filling_the_questionnaire(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the Questionnaires page"):
        app.filling_questionnaire.open_questionnaires_page()

    with step("Deleting a created questionnaires"):

        with step("Go to the page with all the questionnaires"):
            app.filling_questionnaire.open_all_questionnaires_page('Questionnaires')

        with step("Search for a created questionnaire and delete it"):
            app.filling_questionnaire.search_created_questionnaires_and_delete()

        with step("Display a push message about successful removal of the questionnaire"):
            app.filling_questionnaire.push_message_about_successful_removal_questionnaire('questionnaire has been '
                                                                                          'deleted')
