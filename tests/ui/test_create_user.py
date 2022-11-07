from diploma_project_tests.model.authorization import authorization_on_admin_panel
from allure import title, tag, step
from diploma_project_tests.helpers import app
from diploma_project_tests.data.data import *


@tag("Web UI")
@title("Creating user")
def test_add_user(setup_browser):
    browser = setup_browser

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the Users page"):
        app.create_user.open_users_page()

    with step("Checking the 'Manage users' page display"):
        app.create_user.checking_manage_users_page('Manage users')

    with step("Creating user"):
        app.create_user.creat_user()

        with step("Checking the 'ADD NEW USER' pop-up display"):
            app.create_user.checking_add_new_user_pop_up('ADD NEW USER')

        with step("Filling username"):
            app.create_user.add_username(Users.name_user)

        with step("Filling name"):
            app.create_user.add_name(Users.name_user)

        with step("Filling email"):
            app.create_user.add_email(Users.email)

        with step("Filling phone number"):
            app.create_user.add_phone_number(Users.phone_number)

        with step("Filling living area"):
            app.create_user.add_living_area(Users.city)

        with step("Filling password"):
            app.create_user.add_password(Users.password)

        with step("Filling repeat password"):
            app.create_user.add_repeat_password(Users.password)

        with step("Submit the form"):
            app.create_user.submit_form()

        with step("Display a push message about successful create user"):
            app.create_user.push_message_about_successful_create_user('New user has been created')

    with step("Deleting a created user"):
        app.create_user.delete_created_user(Users.name_user)

        with step("Search for a created user and delete it"):
            app.create_user.search_created_user_and_delete(Users.name_user)

        with step("Display a push message about successful removal of the user"):
            app.create_user.push_message_about_successful_removal_user('User has been deleted')
