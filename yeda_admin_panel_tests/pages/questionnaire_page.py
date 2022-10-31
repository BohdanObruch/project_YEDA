import time
import os

from dotenv import load_dotenv
from selene import have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from yeda_admin_panel_tests.controls.utils import resource


class CreateQuestionnaire:

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
        NAME_QUESTIONNAIRE = os.getenv('name_questionnaire')
        s('#title').type(f'{NAME_QUESTIONNAIRE}')
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
        time.sleep(1)
        s('.jodit-dialog__footer .jodit-ui-button_ok').click()
        return self

    def shuffle_questions(self):
        s('.d-inline-block [name="shuffle_questions"]').click()
        return self

    def limit_to_display_count_questions(self, count_questions: int):
        s('.max-q-count [name="questions_count"').clear().type(count_questions)
        return self

    def submit_form(self):
        s('[type="submit"]').click()
        time.sleep(2)
        return self
