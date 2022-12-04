import os
import time

from diploma_project_tests import command
from dotenv import load_dotenv
from selene import have, by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from diploma_project_tests.controls.utils import resource

name_questionnaire = os.getenv('NAME_QUESTIONNAIRE')


class CreateQuestionnairePage:

    def open_questionnaires_page(self):
        s('.elearning-nav-li').click()
        s('.questionnaires-nav-li').click()
        return self

    def checking_questionnaires_page(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def creat_questionnaire(self):
        s('.panel-heading .btn').click()
        return self

    def checking_create_questionnaire_page(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
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
        s('#title').type(f'{name_questionnaire}')
        return self

    def add_short_description(self, short_description: str):
        s('[name="short_descr"]').type(short_description)
        return self

    def add_description(self, description: str):
        s('.jodit-workplace .jodit-wysiwyg').type(' ')
        s('.jodit-ui-group_group_indent .jodit-toolbar-button__trigger').click()
        s('.jodit-toolbar-button_center .jodit-toolbar-button__button').click()
        s('.jodit-workplace .jodit-wysiwyg').type(description).press_enter()
        s('.jodit-ui-group_size_middle .jodit-icon_select_all').click()
        s('.jodit-toolbar-button_bold').click()
        s('.jodit-workplace .jodit-wysiwyg').click()
        s('.jodit-workplace .jodit-wysiwyg').type(' ').press_enter()
        return self

    def add_image(self, picture: str):
        s('.jodit-ui-group__image').click()
        s('[type="file"]').send_keys(resource(picture))
        s('.jodit-wysiwyg img').with_(timeout=15).click()
        return self

    def change_size_picture(self, size_picture: int):
        s('.jodit-toolbar-button_pencil').click()
        s('.imageHeight').clear().type(size_picture)
        s('.jodit-dialog__footer .jodit-ui-button_ok').with_(timeout=5).click()
        return self

    def shuffle_questions(self):
        s('.d-inline-block [name="shuffle_questions"]').click()
        return self

    def limit_to_display_count_questions(self, count_questions: int):
        s('.max-q-count [name="questions_count"').clear().type(count_questions)
        return self

    def submit_form(self):
        s('[type="submit"]').click()
        return self

    def checking_editing_page(self, value):
        s('.page-header').with_(timeout=5).should(have.text(value))
        return self


class FillingQuestionnairePage:

    def open_questionnaires_page(self):
        s('.elearning-nav-li').click()
        s('.questionnaires-nav-li').click()
        return self

    def checking_questionnaires_page(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def open_create_questionnaire(self):
        s(f'//*[text() = "{name_questionnaire}"]').click()
        return self

    def checking_editing_questionnaire_page(self, value):
        s('.page-header').should(have.text(value))
        return self

    def add_first_chapters_title(self, first_title_chapters: str, first_multiplier: int):
        s('.col-md-9 #edit-chapters').click()
        s('#create-chapter [name="title"]').type(first_title_chapters)
        s('#create-chapter [name="multiplier"]').type(first_multiplier)
        s('#create-chapter .btn').click()
        return self

    def add_first_categories(self, first_categories: str):
        s('.create-category [name="new-title"]').type(first_categories)
        s('.create-category .btn').click()
        return self

    def add_first_subcategories(self, subcategories: str):
        s('.create-subcategory [name="new-title"]').type(subcategories)
        s('.create-subcategory .btn').click()
        s('#question_partition_modal .modal-footer .btn').click()
        return self

    def create_new_practice_first_question(self, value):
        s('#questionnaire-chapters').with_(timeout=4).should(have.text(value))
        s('#questionnaire-chapters .questionnaire-chapter-create').click()
        s('#questionnaire-chapters .create_new_question').click()
        return self

    def add_first_question(self, first_resource: str):
        s('.col-sm-6:nth-child(1) .jodit-toolbar-button_image .jodit-toolbar-button__button').click()
        s('.jodit-tab [type="file"]').send_keys(resource(first_resource))
        return self

    def add_solution_explanation(self, second_resource: str):
        s('.col-sm-6:nth-child(2) .jodit-toolbar-button_image .jodit-toolbar-button__button').click()
        s('.jodit-tab [type="file"]').send_keys(resource(second_resource))
        return self

    def add_first_tag(self, name_first_tag: str):
        s('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').type(name_first_tag).press_enter()
        return self

    def add_difficulty_level_one(self):
        s('#difficulty_level_dropdown .dropdown-toggle').click()
        s('#difficulty_level_dropdown .dropdown-menu').element('[data-id="1"]').click()
        return self

    def selected_first_chapters(self):
        s('#questions_chapter_dropdown .dropdown-toggle').click()
        s('#questions_chapter_dropdown .dropdown-menu .dropdown-item').click()
        return self

    def selected_first_category(self):
        s('#questions_category_dropdown .dropdown-toggle').click()
        s('#questions_category_dropdown .dropdown-menu .dropdown-item').click()
        return self

    def selected_first_subcategory(self):
        s('#questions_sub_category_dropdown .dropdown-toggle').click()
        s('#questions_sub_category_dropdown .dropdown-menu .dropdown-item').click()
        return self

    def add_video_to_answer_solution(self, third_resource: str, text_video_transcoding: str):
        s('#video_file').send_keys(resource(third_resource))
        s('#video #vimeo_transcoding_text').with_(timeout=15).should(have.text(text_video_transcoding))
        return self

    def add_first_answer(self, answer_first: int, answer_second: int, answer_third: int, answer_fourth: int):
        s('.answer .text').type(answer_first)
        s('.answer:nth-child(2) .text').type(answer_second)
        s('.answer:nth-child(3) .text').type(answer_third)
        s('.answer:nth-child(4) .text').type(answer_fourth)
        s('.answer:nth-child(1) .question-answers').click()
        return self

    def push_message_about_saving_first_question(self, value):
        s('#add-question-footer .btn-primary').click()
        s('[data-notify="message"]').with_(timeout=4).should(have.text(value))
        return self

    def add_second_chapters_title(self, second_title_chapters: str, second_multiplier: int):
        s('.col-md-9 #edit-chapters').click()
        s('#create-chapter [name="title"]').type(second_title_chapters)
        s('#create-chapter [name="multiplier"]').clear().type(second_multiplier)
        s('#create-chapter .btn').click()
        return self

    def add_second_categories(self, second_categories: str):
        s('.chapter:nth-child(2) .create-category [name="new-title"]').type(second_categories)
        s('.chapter:nth-child(2) .create-category .btn').click()
        s('#question_partition_modal .modal-footer .btn').click()
        return self

    def create_new_practice_second_question(self):
        s('#questionnaire-chapters .create_new_question').click()
        return self

    def add_second_question(self, fourth_resource: str):
        s('.modal-body .jodit-wysiwyg:nth-child(1)').click()
        s('.col-sm-6:nth-child(1) .jodit-toolbar-button_image .jodit-toolbar-button__button').click()
        s('.jodit-tab [type="file"]').send_keys(resource(fourth_resource))
        return self

    def add_second_tag(self, name_second_tag: str):
        s('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').with_(timeout=5).type(name_second_tag).press_enter()
        return self

    def selected_second_chapters(self):
        s('#questions_chapter_dropdown .dropdown-toggle').click()
        s('#questions_chapter_dropdown .dropdown-menu li:nth-child(2)').click()
        return self

    def selected_second_category(self):
        s('#questions_category_dropdown .dropdown-toggle').perform(command.js.scroll_into_view).click()
        s('#questions_category_dropdown .dropdown-menu li:nth-child(2)').click()
        return self

    def add_second_answer(self, first_answer: str, second_answer: str, third_answer: str, fourth_answer: str):
        s('.answer .text').type(first_answer)
        s('.answer:nth-child(2) .text').type(second_answer)
        s('.answer:nth-child(3) .text').type(third_answer)
        s('.answer:nth-child(4) .text').type(fourth_answer)
        s('.answer:nth-child(3) .question-answers').click()
        s('#add-question-footer .btn-primary').click()
        return self

    def push_message_about_saving_second_question(self, value):
        s('[data-notify="message"]').with_(timeout=4).should(have.text(value))
        return self

    def checking_the_number_of_created_questions_first_block(self, value):
        s('.questionnaire-chapter:nth-child(1) .count').with_(timeout=4).should(have.text(value))
        return self

    def create_new_practice_third_question(self, value):
        s('#questionnaire-chapters').with_(timeout=4).should(have.text(value))
        s('#questionnaire-chapters .questionnaire-chapter-create').click()
        s('.questionnaire-chapter:nth-child(2) .create_new_question').click()
        return self

    def add_third_question(self, third_question: str):
        s('.modal-body .col-sm-6:nth-child(1) .jodit-wysiwyg').type(third_question)
        return self

    def add_third_tag(self, name_third_tag: str):
        s('.tags-input-wrapper .bootstrap-tagsinput [type="text"]').type(name_third_tag).press_enter()
        return self

    def add_difficulty_level_second(self):
        s('#difficulty_level_dropdown .dropdown-toggle').click()
        s('#difficulty_level_dropdown .dropdown-menu').element('[data-id="2"]').click()
        return self

    def changing_the_question_type(self):
        s('#typeDropdownMenuButton').click()
        s('.dropdown-menu [data-type="checkbox"]').click()
        return self

    def add_third_answer(self, first_answer_third_question: str, second_answer_third_question: str,
                         third_answer_third_question: str, fourth_answer_third_question: str,
                         fifth_answer_third_question: str,
                         sixth_answer_third_question: str, seventh_answer_third_question: str,
                         eighth_answer_third_question: str):
        s('.answer .text').type(first_answer_third_question)
        s('.answer:nth-child(2) .text').type(second_answer_third_question)
        s('.answer:nth-child(3) .text').type(third_answer_third_question)
        s('.answer:nth-child(4) .text').type(fourth_answer_third_question)
        s('.answer:nth-child(5) [type="text"]').perform(command.js.scroll_into_view)
        s('.answer:nth-child(5) .text').type(fifth_answer_third_question).click()
        s('.answer:nth-child(6) .text').type(sixth_answer_third_question).click()
        s('.answer:nth-child(7) .text').type(seventh_answer_third_question).click()
        s('.answer:nth-child(8) .text').type(eighth_answer_third_question).click()
        s('.answer:nth-child(8) .text').perform(command.js.scroll_into_view).click()
        return self

    def indicating_the_correct_answer(self):
        s('.answer:nth-child(2) .question-answers').click()
        s('.answer:nth-child(4) .question-answers').click()
        s('.answer:nth-child(6) .question-answers').click()
        s('.answer:nth-child(8) .question-answers').click()
        s('#add-question-footer .btn-primary').click()
        return self

    def push_message_about_saving_third_question(self, value):
        s('[data-notify="message"]').with_(timeout=4).should(have.text(value))
        return self

    def checking_the_number_of_created_questions_second_block(self, value):
        s('.questionnaire-chapter:nth-child(2) .count').with_(timeout=4).should(have.text(value))
        return self

    def create_new_practice_fourth_question(self, value):
        s('#questionnaire-chapters').with_(timeout=4).should(have.text(value))
        s('#questionnaire-chapters .questionnaire-chapter-create').click()
        s('.questionnaire-chapter:nth-child(3) .add-question').click()
        return self

    def importing_questions_from_other_questionnaires(self):
        s('#search-questions-list [data-id="76"]').click()
        s('#search-questions-list [data-id="78"]').click()
        s('#search-questions-list [data-id="62"]').click()
        s('.modal-footer #sq_save').click()
        return self

    def checking_the_number_of_created_questions_third_block(self, value):
        s('.questionnaire-chapter:nth-child(3) .count').with_(timeout=4).should(have.text(value))
        return self

    def add_first_title_questionnaire_chapters(self, first_questionnaire_title: str):
        s('.list .questionnaire-chapter:nth-child(1) .edit').click()
        s('.list .questionnaire-chapter:nth-child(1) .chapter-name').type(first_questionnaire_title)
        s('.list .questionnaire-chapter:nth-child(1) .save').click()
        return self

    def add_second_title_questionnaire_chapters(self, second_questionnaire_title: str):
        s('.list .questionnaire-chapter:nth-child(2) .edit').click()
        s('.list .questionnaire-chapter:nth-child(2) .chapter-name').type(second_questionnaire_title)
        s('.list .questionnaire-chapter:nth-child(2) .save').click()
        return self

    def add_third_title_questionnaire_chapters(self, third_questionnaire_title: str):
        s('.list .questionnaire-chapter:nth-child(3) .edit').click()
        s('.list .questionnaire-chapter:nth-child(3) .chapter-name').type(third_questionnaire_title)
        s('.list .questionnaire-chapter:nth-child(3) .save').click()
        return self

    def delete_first_chapters(self):
        s('.col-md-9 #edit-chapters').click()
        s('#chapters .chapter .delete').with_(timeout=4).click()
        s('.container .btn:nth-child(1)').click()
        return self

    def delete_second_chapters(self):
        s('#chapters .chapter:nth-child(2)').with_(timeout=4).should(be.not_.visible)
        s('#chapters .chapter .delete').with_(timeout=4).click()
        s('.container .btn:nth-child(1)').click()
        return self

    def checking_the_removal_of_chapters(self):
        s('#chapters').should(be.not_.visible)
        s('#question_partition_modal .modal-footer .btn').click()
        return self

    def open_all_questionnaires_page(self, value):
        s('.questionnaires-nav-li').click()
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def search_created_questionnaires_and_delete(self):
        s('.filter #search_text').type(name_questionnaire).press_enter()
        s('#sortable .questionnaire-link').with_(timeout=5).should(have.text(name_questionnaire))
        s('#sortable .questionnaire-delete').click()
        s('.jconfirm-box .btn:nth-child(1)').with_(timeout=5).click()
        return self

    def push_message_about_successful_removal_questionnaire(self, value):
        s('[data-notify="message"]').with_(timeout=5).should(have.text(value))
        return self
