from selene.support.shared import browser
from yeda_admin_panel_tests.controls.utils import resource
from yeda_admin_panel_tests.model.authorization import authorization_on_admin_panel
from allure import title, tag, step
from yeda_admin_panel_tests.helpers import app
from yeda_admin_panel_tests.data.data import *


@tag("Web UI")
@title("Creating an questionnaire")
def test_create_questionnaire(setup_browser):
    # browser = setup_browser

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the Questionnaires page"):
        app.create_questionnaire.open_questionnaires_page()

    with step("Checking the Questionnaires page display"):
        app.create_questionnaire.checking_questionnaires_page('Questionnaires')

    with step("Creating a questionnaire"):
        app.create_questionnaire.creat_questionnaire()

        with step("Checking the Adding Questionnaire page display"):
            app.create_questionnaire.checking_create_questionnaire_page('Adding Questionnaire')

        with step("Changing the status to active to display on the site"):
            app.create_questionnaire.change_status()

        with step("Choose a category"):
            app.create_questionnaire.add_category()

        with step("Filling in the title"):
            app.create_questionnaire.add_title()

        with step("Filling a short description"):
            app.create_questionnaire.add_short_description(Questionnaire.short_description)

        with step("Filling a description"):
            app.create_questionnaire.add_description(Questionnaire.description)

            with step("Adding image"):
                app.create_questionnaire.add_image(Questionnaire.picture)

                with step("Changing the size of an added image"):
                    app.create_questionnaire.change_size_picture(Questionnaire.size_picture)

        with step("Mark indications 'Shuffle questions'"):
            app.create_questionnaire.shuffle_questions()

            with step("Specifying the limit to display"):
                app.create_questionnaire.limit_to_display_count_questions(Questionnaire.count_questions)

    with step("Submit the form"):
        app.create_questionnaire.submit_form()
