from selene import have, command
from selene.support.shared.jquery_style import s


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
        s('#app-user-form #edit_phone').type(phone_number)
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
        return self

    def delete_created_user(self, name_user: str):
        s('.filter #search_text').with_(timeout=5).type(name_user)
        return self

    def search_created_user_and_delete(self, name_user: str):
        panel = s('.table').with_(timeout=12)
        panel.all('tr').element_by_its('.username', have.exact_text(name_user)).element('.delete')\
            .perform(command.js.scroll_into_view).click()
        s('.container .btn:nth-child(1)').with_(timeout=5).click()
        return self

    def push_message_about_successful_removal_user(self, value):
        s('[data-notify="message"]').with_(timeout=12).should(have.text(value))
        return self
