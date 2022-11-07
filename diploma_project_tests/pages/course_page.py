import time
import os

from diploma_project_tests import command
from dotenv import load_dotenv
from selene import have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from diploma_project_tests.controls.utils import resource


class CreateCourse:

    def open_courses_page(self):
        s('[href="/admin/courses"]').click()
        return self

    def creat_course(self):
        s('[yedaoldadminhref="elearning/courses/create"]').click()
        return self

    def change_status(self):
        s('#dropdownMenuButton').click()
        s('[data-status-id="3"]').click()
        return self

    def add_category(self):
        s('#dropdown-category').click()
        s('[data-category-id="115"]').click()
        return self

    def add_title(self):
        NAME_COURSE = os.getenv('name_course')
        s('#name').type(f'{NAME_COURSE}')
        return self

    def add_slug(self):
        s('#generate-slug').click()
        return self

    def add_short_description(self, short_description: str):
        s('[name="short_descr"]').type(short_description)
        return self

    def add_description(self, description: str):
        s('[name="descr"]').type(description)
        return self

    def add_duration(self, duration: str):
        s('[name="duration"]').type(duration)
        return self

    def add_prerequisites(self, prerequisites: str):
        s('[name="prerequisites"]').type(prerequisites)
        return self

    def add_video(self, value):
        s('[name="video_link"]').type(value)
        return self

    def add_teaser_image(self, image: str):
        s('#course_photo').send_keys(resource(image))
        return self

    def add_about_course(self, description_line1: str, description_line2: str):
        s('.jodit-wysiwyg').type(description_line1).press_enter()
        s('.jodit-wysiwyg').type(description_line2).press_enter()
        s('.panel-body .jodit-status-bar__item .jodit-toolbar-button__button').click()
        s('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
        return self

    def add_associated_files(self, file: str, table: str):
        s('[name="show_files_to_students"]').click()
        s('#files_input').send_keys(resource(table))
        s('#files_input').send_keys(resource(file))
        time.sleep(2)
        return self

    def add_seo(self, seo_title: str, seo_description: str, seo_author: str):
        s('[name="meta_title"]').type(seo_title)
        s('[name="meta_description"]').type(seo_description)
        s('[name="meta_author"]').type(seo_author)
        return self

    def add_start_date(self, start_date: str):
        s('#date_begin_date').type(start_date).press_tab()
        return self

    def add_end_date(self, end_date: str):
        s('#date_end_date').type(end_date).press_tab()
        return self

    def add_price(self, normal_price: int, discount_price: int):
        s('[name="normal_price"]').type(normal_price)
        s('[name="discount_price"]').type(discount_price)
        return self

    def submit_form(self):
        s('[type="submit"]').click()
        return self

    def check_page_title(self, value):
        s('.page-header').with_(timeout=10).should(have.text(value))
        return self

    def open_all_courses_page(self, value):
        URL_COURSES = os.getenv('url_courses')

        s(f'[href="{URL_COURSES}"]').perform(command.js.click)
        s('#portal-header-default').with_(timeout=10).should(have.text(value))
        return self

    def search_created_course_and_delete(self):
        NAME_COURSE = os.getenv('name_course')

        table = browser.element('#cdk-drop-list-0')
        table.all('.air-list-item').element_by_its('[airtablelikecell="course-name"]',
                                                   have.exact_text(f'{NAME_COURSE}')) \
            .element('.color-danger.clear').click()
        s('// *[text() = "Confirm delete"]').click()
        time.sleep(2)
        return self

    def checking_that_the_course_has_been_deleted(self):
        NAME_COURSE = os.getenv('name_course')
        table = browser.element('#cdk-drop-list-0')
        table.all('.air-list-item').element_by_its('[airtablelikecell="course-name"',
                                                   not have.exact_text(f'{NAME_COURSE}'))
        return self
