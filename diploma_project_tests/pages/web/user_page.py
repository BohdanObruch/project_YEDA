import time

from dotenv import load_dotenv
from selene import have, by
from diploma_project_tests import command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from diploma_project_tests.controls.utils import resource


class CreateUserPage:

    def open_users_page(self):
        s('.users-nav-li').click()
        return self

    def checking_manage_users_page(self, value):
        s('.page-header').should(have.text(value))
        return self

    def creat_user(self):
        s('[data-target="#create-user-modal"').click()
        return self

    def checking_add_new_user_pop_up(self, value):
        s('.modal-title').should(have.text(value))
        return self

    def add_username(self, name_user: str):
        s('#app-user-form #edit_username').type(name_user)
        return self

    def add_name(self, name_user: str):
        s('#app-user-form #edit_name').type(name_user)
        return self

    def add_email(self, email: str):
        s('#app-user-form #edit_email').type(email)
        return self

    def add_phone_number(self, phone_number: int):
        browser.element('#app-user-form #edit_phone').type(phone_number)
        return self

    def add_living_area(self, city: str):
        s('#app-user-form #edit_city').type(city)
        return self

    def add_password(self, password: int):
        s('#app-user-form #password').type(password)
        return self

    def add_repeat_password(self, password: int):
        s('#app-user-form #password_auth').type(password)
        return self

    def submit_form(self):
        s('[type="submit"]').click()
        return self

    def push_message_about_successful_create_user(self, value):
        s('[data-notify="message"]').with_(timeout=20).should(have.text(value))
        time.sleep(3)
        return self

    def delete_created_user(self, name_user: str):
        s('.filter #search_text').type(name_user)
        return self

    def search_created_user_and_delete(self, name_user: str):
        time.sleep(1)
        panel = browser.element('.table')
        panel.all('tr').element_by_its('.username', have.exact_text(name_user)).element('.delete').click()
        s('.container .btn:nth-child(1)').click()
        return self

    def push_message_about_successful_removal_user(self, value):
        s('[data-notify="message"]').with_(timeout=5).should(have.text(value))
        return self
