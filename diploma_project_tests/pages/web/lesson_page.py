from dotenv import load_dotenv
from selene import have, by
from diploma_project_tests import command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from diploma_project_tests.controls.utils import resource


class CreateLessonPage:

    def open_lessons_page(self, value):
        s('.elearning-nav-li').click()
        s('.lessons-nav-li').click()
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def creat_a_lesson(self):
        s('.panel-heading .btn').click()
        return self

    def checking_lesson_page_title(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def chang_status(self):
        s('#dropdownMenuButton').click()
        s('[data-status-id="3"]').click()
        return self

    def add_category(self):
        s('#dropdown-category').click()
        s('[data-category-id="115"]').click()
        return self

    def add_price(self, normal_price: int, discount_price: int):
        s('[name="normal_price"]').type(normal_price)
        s('[name="discount_price"]').type(discount_price)
        return self

    def add_title(self, title_lesson: str):
        s('.form-group #title').type(title_lesson)
        return self

    def add_description(self, description_text: str):
        s('.jodit-workplace .jodit-wysiwyg').type(description_text)
        return self

    def submit_form(self):
        s('#save-lesson').click()
        return self

    def show_date_edited(self):
        s('#show_date_edited').click()
        return self

    def add_files(self, document: str, table: str):
        s('.lesson-files-block #lesson_files_input').send_keys(resource(document))
        s('#files-tbody .file-to-speech').click()
        s('.lesson-files-block #lesson_files_input').send_keys(resource(table))
        return self

    def add_lecturer(self, name_lecturer: str):
        s('#save-lesson').perform(command.js.scroll_into_view)
        s('.lector-name').type(name_lecturer)
        s('.suggestions [data-id="48"]').with_(timeout=5).click()
        s('.add_lecturer').click()
        return self

    def add_first_part_of_lesson(self):
        s('.add-video').click()
        s('.open-video-collapse .lesson-part-toggle').click()
        return self

    def add_title_first_part(self, title_first_part_lesson: str):
        s('#lesson_part1 .page_video_title').type(title_first_part_lesson)
        return self

    def add_video_first_part(self, video_first_part_lesson: str):
        s('.lesson_video_file').send_keys(resource(video_first_part_lesson))
        return self

    def text_to_speech(self):
        s('.checkbox-span .summary_to_speech_input').click()
        return self

    def not_show_the_about_text(self):
        s('.hide_text_if_there_is_speech_input').click()
        return self

    def checking_the_video_upload_part_one(self, text_message: str):
        s('#save-lesson').perform(command.js.scroll_into_view)
        s('.vimeo_transcoding_text').with_(timeout=15).should(have.text(text_message))
        return self

    def save_first_part_lesson(self):
        s('#save-lesson').click()
        return self

    def close_first_part_block(self):
        s('.open-video-collapse .lesson-part-toggle').click()
        return self

    def add_second_part_of_lesson(self):
        s('.add-video').perform(command.js.click)
        s('.lesson-video:nth-child(2) .lesson-part-toggle').with_(timeout=5).click()
        return self

    def add_title_second_part(self, title_second_part_lesson: str):
        s('.lesson-video:nth-child(2) .page_video_title').type(title_second_part_lesson)
        return self

    def add_video_second_part(self, video_second_part_lesson: str):
        s('.lesson-video:nth-child(2) .lesson_video_file').send_keys(resource(video_second_part_lesson))
        return self

    def checking_the_video_upload_second_part(self, text_message: str):
        s('#save-lesson').perform(command.js.scroll_into_view)
        s('.lesson-video:nth-child(2) .vimeo_transcoding_text').with_(timeout=15).should(have.text(text_message))
        return self

    def save_second_part_lesson(self):
        s('#save-lesson').click()
        return self

    def close_second_part_block(self):
        s('.lesson-video:nth-child(2) .lesson-part-toggle').click()
        return self

    def moving_blocks_of_parts(self):
        first_part = s('#lesson_parts_accordion .lesson-video:nth-child(1) .col').with_(timeout=5)
        second_part = s('#lesson_parts_accordion .lesson-video:nth-child(2) .lesson-video-handle')
        second_part.perform(command.drag_to(first_part))
        s('#save-lesson').click()
        return self

    def search_created_lesson(self, name_lesson: str, title_lesson: str):
        s('[data-name="title"').type(name_lesson)
        s('.ui-sortable-handle .col').with_(timeout=6).should(have.text(title_lesson)).click()
        return self

    def delete_created_lesson(self, name_lesson: str, title_lesson: str):
        s('[data-name="title"').type(name_lesson)
        s('.ui-sortable-handle .col').with_(timeout=6).should(have.text(title_lesson))
        s('.ui-sortable-handle .delete').click()
        s('.container .btn:nth-child(1)').with_(timeout=5).click()
        return self

    def push_message_about_successful_removal_lesson(self, value):
        s('[data-notify="message"]').with_(timeout=5).should(have.text(value))
        return self

