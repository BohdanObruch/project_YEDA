import os
import time

from dotenv import load_dotenv
from selene import have, by
from selene.core import command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from yeda_admin_panel_tests.controls.utils import resource


class CreateBundles:

    def open_bundles_page(self, value):
        URL_BUNDLES = os.getenv('url_bundles')

        s(f'[href="{URL_BUNDLES}"]').click()
        s('.page-header').should(have.text(value))
        s('.btn.btn-primary').click()
        return self

    def checking_adding_bundle_page(self, value):
        s('.page-header').should(have.text(value))
        return self

    def add_title(self):
        NAME_BUNDLE = os.getenv('name_bundle_ui')
        s('#name').type(f'{NAME_BUNDLE}')
        return self

    def add_duration(self, value):
        s('[name="duration"]').type(value)
        return self

    def add_prerequisites(self, value):
        s('[name="prerequisites"]').type(value)
        return self

    def add_video(self, value):
        s('[name="video_link"]').type(value)
        return self

    def add_short_description(self, value):
        s('[name="description"]').type(value)
        return self

    def add_description(self, description_line1: str, description_line2: str):
        s('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
        s('.jodit-wysiwyg').type(description_line1).press_enter()
        s('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
        s('.jodit-wysiwyg').type(description_line2).press_enter()
        return self

    def add_associated_files(self, picture: str, video: str):
        s('#bundle_files_input').send_keys(resource(picture))
        s('#bundle_files_input').send_keys(resource(video))
        return self

    def change_status(self):
        s('#status-bundle-dropdown').click()
        s('[data-status-id="3"]').click()
        return self

    def add_category(self):
        s('.panel-body .checkbox.col-12.w-100 [value="10"]').click()
        s('.panel-body .checkbox.col-12.w-100 [value="115"]').click()
        return self

    def add_teaser_image(self, picture: str):
        s('.image_upload_bundle').send_keys(resource(picture))
        return self

    def add_seo(self, seo_title: str, seo_description: str):
        s('[name="seo[meta_title]"]').type(seo_title)
        s('[name="seo[meta_description]"]').type(seo_description)
        s('#bundle-generate-slug').click()
        return self

    def add_start_date(self, start_date: str):
        s('#date_begin_date').type(start_date).press_tab()
        return self

    def add_end_date(self, end_date: str):
        s('#date_end_date').type(end_date).press_tab()
        return self

    def add_price(self, normal_price: int, discount_price: int):
        s('[name="price"]').type(normal_price)
        s('[name="discount_price"]').type(discount_price)
        return self

    def submit_form(self):
        s('[type="submit"]').click()
        return self

    def check_page_title(self, value):
        browser.element('.page-header').with_(timeout=20).should(have.text(value))
        return self


class FillingBundles:
    def open_bundles_page(self, value):
        URL_BUNDLES = os.getenv('url_bundles')

        s(f'[href="{URL_BUNDLES}"]').click()
        s('.page-header').should(have.text(value))
        return self

    def open_create_bundle(self):
        NAME_BUNDLE = os.getenv('name_bundle_ui')

        s(f'//*[text() = "{NAME_BUNDLE}"]').click()
        return self

    def checking_editing_bundle_page(self, value):
        s('.page-header').should(have.text(value))
        return self

    def add_students(self, file_with_users: str):
        s('.panel [data-target="#students-collapse"] .fa-plus').click()
        s('#students-collapse #import_users_file').send_keys(resource(file_with_users))
        s('.import-student:nth-child(1) .remove-from-import').click()
        s('.jconfirm-buttons .btn-default:nth-child(1)').click()
        s('.import-student:nth-child(3) .remove-from-import').click()
        s('.jconfirm-buttons .btn-default:nth-child(1)').click()
        s('.students-import #import-students').click()
        time.sleep(4)
        return self

    def open_courses_block(self):
        s('.panel [data-target="#courses-collapse"] .fa-plus').click()
        return self

    def add_first_course(self, name_first_course: str, full_name_first_course: str):
        s('.forum-form #find-course').type(name_first_course)
        s('.forum-form #course-suggestions').element('[data-id="196"]').click()
        s('#courses-collapse #add-course').click()
        s('#bundle-course-item-196 .text-right').with_(timeout=3).should(have.text(full_name_first_course))
        return self

    def mark_that_the_mandatory_first_course(self):
        s('#bundle-course-item-196 .course-is-required').click()
        return self

    def date_when_first_course_available(self):
        s('#bundle-course-item-196 .date-start-bundle-course').click()
        s('.ui-datepicker-next').click().element('//*[text() = "29"]').click()
        return self

    def date_when_first_course_be_closed(self, date_closed_first_course: str):
        s('#bundle-course-item-196 .date-end-bundle-course').click()
        s('.ui-datepicker-next').click()
        s('//*[text() = "15"]').click()  # November 15
        s('#bundle-course-item-196 .date-end-bundle-course').with_(timeout=5)\
            .should(have.value(date_closed_first_course))
        return self

    def add_second_course(self, name_second_course: str, full_name_second_course: str):
        s('.forum-form #find-course').type(name_second_course)
        s('.forum-form #course-suggestions').element('[data-id="195"]').click()
        s('#courses-collapse #add-course').click()
        s('#bundle-course-item-195 .text-right').with_(timeout=3).should(have.text(full_name_second_course))
        return self

    def mark_that_the_mandatory_second_course(self):
        s('#bundle-course-item-195 .course-is-required').click()
        return self

    def date_when_second_course_available(self):
        s('#bundle-course-item-195 .date-start-bundle-course').click()
        s('.ui-datepicker-next').click()
        # s('.ui-datepicker-next').click()
        s('//*[text() = "20"]').click()
        return self

    def date_when_second_course_be_closed(self, date_closed_second_course: str):
        s('#bundle-course-item-195 .date-end-bundle-course').click()
        s('.ui-datepicker-next').click()
        s('.ui-datepicker-next').click()
        # s('.ui-datepicker-next').click()
        s('//*[text() = "10"]').click()
        s('#bundle-course-item-195 .date-end-bundle-course').with_(timeout=5)\
            .should(have.value(date_closed_second_course))
        return self

    def open_all_bundles_page(self, value):
        URL_BUNDLES = os.getenv('url_bundles')

        s(f'[href="{URL_BUNDLES}"]').perform(command.js.click)
        s('.page-header').with_(timeout=7).should(have.text(value))
        return self

    def search_created_bundle_and_delete(self):
        NAME_BUNDLE = os.getenv('name_bundle_ui')

        panel = browser.element('.panel-body')
        panel.all('.row').element_by_its('.course-link', have.exact_text(f'{NAME_BUNDLE}')).element('.delete').click()
        s('.container .btn:nth-child(1)').click()
        return self

    def push_message_about_successful_removal_bundle(self, value):
        s('[data-notify="message"]').with_(timeout=5).should(have.text(value))
        return self
