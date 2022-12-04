from diploma_project_tests.model.authorization import authorization_on_admin_panel
from allure import title, tag, step
from diploma_project_tests.helpers import app
from diploma_project_tests.data.data import *


def test_add_teacher(setup_browser):

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the Teachers page"):
        app.create_teacher.open_teachers_page()

    with step("Checking the 'Teachers' page display"):
        app.create_teacher.checking_teachers_page('Teachers')

    with step("Creating teacher"):
        app.create_teacher.creat_teacher()

        with step("Checking the Create Teacher page display"):
            app.create_teacher.checking_create_teacher_page('Create Teacher')

        with step("Adding teaser images"):
            app.create_teacher.add_teaser_image(Teacher.picture)

        with step("Adding SEO"):
            app.create_teacher.add_seo(Teacher.seo_title, Teacher.seo_description)

        with step("Adding name teacher"):
            app.create_teacher.add_name(Teacher.name_teacher)

        with step("Adding positions teacher"):
            app.create_teacher.add_positions(Teacher.positions_teacher)

        with step("Filling a short description"):
            app.create_teacher.add_short_description(Teacher.short_description)

        with step("Filling a description"):
            app.create_teacher.add_description(Teacher.description)

        with step("Filling email"):
            app.create_teacher.add_email(Teacher.email)

        with step("Filling phone number"):
            app.create_teacher.add_phone_number(Teacher.phone_number)

    with step("Submit the form"):
        app.create_teacher.submit_form()

    with step("Checking_title_page"):
        app.create_teacher.checking_title_page('Edit Teacher')

    with step("Deleting a created Teacher"):
        with step("Go to the Teachers page"):
            app.create_teacher.open_all_teachers_page()

        with step("Search for a created teacher and delete it"):
            app.create_teacher.search_created_teacher_and_delete(Teacher.name_teacher)

            with step("Display a push message about successful removal of the teacher"):
                app.create_teacher.push_message_about_successful_removal_teacher('Teacher has been deleted')
