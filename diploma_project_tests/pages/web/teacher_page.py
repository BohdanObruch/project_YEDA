import time

from selene import have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from diploma_project_tests.controls.utils import resource


class CreateTeacherPage:

    def open_teachers_page(self):
        s('.elearning-nav-li').click()
        s('.teachers-nav-li').click()
        return self

    def checking_teachers_page(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def creat_teacher(self):
        s('.panel-heading .btn').click()
        return self

    def checking_create_teacher_page(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def add_teaser_image(self, picture: str):
        s('.upload_button #photo').send_keys(resource(picture))
        return self

    def add_seo(self, seo_title: str, seo_description: str):
        s('#seo-collapse [name="meta_title"]').type(seo_title)
        s('#seo-collapse [name="meta_description"]').type(seo_description)
        return self

    def add_name(self, name_teacher: str):
        s('#name').type(name_teacher)
        return self

    def add_positions(self, positions_teacher: str):
        s('[name="positions"]').type(positions_teacher)
        return self

    def add_short_description(self, short_description: str):
        s('[name="short_descr"]').type(short_description)
        return self

    def add_description(self, description: str):
        s('[name="about"]').type(description)
        return self

    def add_email(self, email: str):
        s('[name="email"]').type(email)
        return self

    def add_phone_number(self, phone_number: int):
        s('[name="phone"]').type(phone_number)
        return self

    def submit_form(self):
        s('[type="submit"]').click()
        return self

    def checking_title_page(self, value):
        s('.page-header').with_(timeout=5).should(have.text(value))
        return self

    def open_all_teachers_page(self):
        s('.teachers-nav-li').click()
        return self

    def search_created_teacher_and_delete(self, name_teacher: str):

        s('.filter #search_text').type(name_teacher).press_enter()
        s(f'//*[text() = "{name_teacher}"]').with_(timeout=5).should(have.text(name_teacher))
        time.sleep(3)
        table = browser.element('.table')
        table.all('tr').element_by_its('.teacher-name', have.exact_text(name_teacher)) \
            .element('.delete').click()
        s('.container .btn:nth-child(1)').click()
        return self

    def push_message_about_successful_removal_teacher(self, value):
        s('[data-notify="message"]').with_(timeout=5).should(have.text(value))
        return self
