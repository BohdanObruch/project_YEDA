import time

from selene import command
from selene import have
from selene.support.shared.jquery_style import s
from diploma_project_tests.controls.utils import resource
from tests.conftest import dotenv

name_course = dotenv.get('NAME_COURSE')
url_courses = dotenv.get('URL_COURSES')


class CreateCoursePage:

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
        s('[data-category-id="115"]').with_(timeout=3) \
            .perform(command.js.scroll_into_view).click()
        return self

    def add_title(self):
        s('#name').type(f'{name_course}')
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
        s('.jodit-status-bar button[type="button"]').perform(command.js.scroll_into_view).click()
        s('.jodit-toolbar-button_bold button[type="button"]').click()
        return self

    def add_associated_files(self, file: str, table: str):
        s('[name="show_files_to_students"]').click()
        s('#files_input').send_keys(resource(table))
        s('#files_input').with_(timeout=10).send_keys(resource(file))
        return self

    def add_seo(self, seo_title: str, seo_description: str, seo_author: str):
        s('[name="meta_title"]').with_(timeout=5).type(seo_title)
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
        s(f'[href="{url_courses}"]').perform(command.js.click)
        s('#portal-header-default').with_(timeout=10).should(have.text(value))
        return self

    def search_created_course_and_delete(self):
        table = s('#cdk-drop-list-0').with_(timeout=10)
        table.all('.air-list-item').with_(timeout=10).element_by_its('[airtablelikecell="course-name"]',
                                                                     have.exact_text(f'{name_course}')).element(
            '.color-danger.clear').click()
        s('// *[text() = "Confirm delete"]').click()
        return self

    def checking_that_the_course_has_been_deleted(self):
        table = s('#cdk-drop-list-0').with_(timeout=10)
        table.all('.air-list-item').with_(timeout=30).element_by_its('[airtablelikecell="course-name"]',
                                                                     have.no.value(f'{name_course}'))
        time.sleep(3)
        return self
