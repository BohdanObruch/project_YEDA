import time
import lorem

from selene import have, command
from selene.support.shared.jquery_style import s

content_survey = lorem.paragraph()


class SurveyPage:

    def open_surveys_page(self):
        s('.elearning-nav-li').click()
        s('.surveys-nav-li').click()
        return self

    def checking_the_display_of_the_surveys_page(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def creat_survey(self):
        s('.panel-heading .btn').click()
        return self

    def checking_title_survey_page(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def add_title(self, name_survey: str):
        s('#survey-title').type(name_survey)
        return self

    def add_opening_text(self):
        s('#store_survey_form div:nth-child(4) .jodit-wysiwyg').type(content_survey)
        return self

    def add_final_text(self, final_text: str):
        s('#store_survey_form div:nth-child(5) .jodit-wysiwyg').type(final_text)
        return self

    def change_status(self):
        s('#is_active').perform(command.js.scroll_into_view).click()
        return self

    def submit_form(self):
        s('#store_survey_form .btn-primary').perform(command.js.scroll_into_view).click()
        return self

    def checking_editing_survey_page(self, value):
        s('.page-header').with_(timeout=4).should(have.text(value))
        return self

    def checking_questions_tab_open(self, value):
        s('.panel:nth-child(2) .panel-heading .panel-title').should(have.text(value))
        return self

    def add_first_questions_type_text(self, message_notification: str, first_question_type: str):
        s('#questions-panel #survey-new-question').click()
        s('[data-notify="message"]').with_(timeout=10).should(have.text(message_notification))
        s('.survey-question:nth-child(1) .panel-title').with_(timeout=10).should(have.text(first_question_type))
        return self

    def add_first_question_content(self, content_first_question: str):
        s('#survey-questions .jodit-wysiwyg').type(content_first_question)
        time.sleep(0.7)
        return self

    def add_number_of_characters_to_answer(self, number_of_characters: int):
        s('#survey-question-number-of-characters').clear().type(number_of_characters)
        return self

    def add_mandatory_first_question_and_add_the_next_button(self):
        s('#survey-questions .survey-question-is-mandatory').click()
        s('#survey-questions .survey-question-do-show-next').click()
        return self

    def add_second_questions_type_paragraph(self, message_notification: str, second_question_type: str):
        s('.panel-body #survey-new-question-type').click()
        s('#survey-new-question-type [value="paragraph"]').click()
        s('#questions-panel #survey-new-question').click()
        s('.survey-question:nth-child(2) .panel-title').should(have.text(second_question_type))
        s('[data-notify="message"]').with_(timeout=3).should(have.text(message_notification))
        time.sleep(0.7)
        return self

    def add_second_question_content(self, content_second_question: str):
        s('#survey-questions .survey-question:nth-child(2) .jodit-wysiwyg').type(content_second_question)
        return self

    def add_third_questions_type_single_choice(self, message_notification: str, third_question_type: str):
        s('.panel-body #survey-new-question-type').click()
        s('#survey-new-question-type [value="single-choice"]').click()
        s('#questions-panel #survey-new-question').click()
        s('.survey-question:nth-child(3) .panel-title').should(have.text(third_question_type))
        s('[data-notify="message"]').with_(timeout=3).should(have.text(message_notification))
        time.sleep(0.7)
        return self

    def add_third_question_content(self, content_third_question: str):
        s('#survey-questions .survey-question:nth-child(3) .jodit-wysiwyg').type(content_third_question)
        return self

    def add_answers_to_third_question(self, first_answer: str, second_answer: str, third_answer: str):
        s('.survey-question:nth-child(3) .input-group:nth-child(1) .survey-question-choice').with_(timeout=10)\
            .perform(command.js.scroll_into_view).click()
        time.sleep(0.9)
        s('.survey-question:nth-child(3) .input-group:nth-child(1) .survey-question-choice').with_(timeout=10)\
            .type(first_answer)
        s('.survey-question:nth-child(3) .input-group:nth-child(2) .survey-question-choice').click()
        time.sleep(0.9)
        s('.survey-question:nth-child(3) .input-group:nth-child(2) .survey-question-choice').type(second_answer)
        s('.survey-question:nth-child(3) .input-group:nth-child(3) .survey-question-choice').click()
        time.sleep(0.9)
        s('.survey-question:nth-child(3) .input-group:nth-child(3) .survey-question-choice').type(third_answer)
        return self

    def add_fourth_questions_type_multiple_choice(self, fourth_question_type: str):
        s('.panel-body #survey-new-question-type').click()
        s('#survey-new-question-type [value="multiple-choice"]').click()
        s('#questions-panel #survey-new-question').click()
        s('.survey-question:nth-child(4) .panel-title').should(have.text(fourth_question_type))
        time.sleep(0.7)
        return self

    def add_fourth_question_content(self, content_fourth_question: str):
        s('.survey-question:nth-child(4) .jodit-wysiwyg').type(content_fourth_question)
        return self

    def add_answers_to_fourth_question(self, first_answer_option: str, second_answer_option: str,
                                       third_answer_option: str, fourth_answer_option: str,
                                       fifth_answer_option: str, sixth_answer_option: str,
                                       seventh_answer_option: str):
        s('.survey-question:nth-child(4) .input-group:nth-child(1) '
          '.survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(4) .input-group:nth-child(1) .survey-question-choice') \
            .type(first_answer_option)
        s('.survey-question:nth-child(4) .input-group:nth-child(2) .survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(4) .input-group:nth-child(2) .survey-question-choice') \
            .type(second_answer_option)
        s('.survey-question:nth-child(4) .input-group:nth-child(3) .survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(4) .input-group:nth-child(3) .survey-question-choice') \
            .type(third_answer_option)
        s('.survey-question:nth-child(4) .input-group:nth-child(4) .survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(4) .input-group:nth-child(4) .survey-question-choice') \
            .type(fourth_answer_option)
        s('.survey-question:nth-child(4) .input-group:nth-child(5) .survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(4) .input-group:nth-child(5) .survey-question-choice') \
            .type(fifth_answer_option)
        s('.survey-question:nth-child(4) .input-group:nth-child(6) .survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(4) .input-group:nth-child(6) .survey-question-choice') \
            .type(sixth_answer_option)
        s('.survey-question:nth-child(4) .input-group:nth-child(7) .survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(4) .input-group:nth-child(7) .survey-question-choice') \
            .type(seventh_answer_option)
        return self

    def add_fifth_questions_type_select_from_list(self, fifth_question_type: str):
        s('.panel-body #survey-new-question-type').click()
        s('#survey-new-question-type [value="select-from-list"]').click()
        s('#questions-panel #survey-new-question').click()
        s('.survey-question:nth-child(5) .panel-title').perform(command.js.scroll_into_view)
        s('.survey-question:nth-child(5) .panel-title').should(have.text(fifth_question_type))
        time.sleep(0.7)
        return self

    def add_fifth_question_content(self, content_fifth_question: str):
        s('.survey-question:nth-child(5) .jodit-wysiwyg').type(content_fifth_question)
        return self

    def add_answers_to_fifth_question(self, first_answer_variant: str, second_answer_variant: str,
                                      third_answer_variant: str):
        s('.survey-question:nth-child(5) .input-group:nth-child(1) .survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(5) .input-group:nth-child(1) .survey-question-choice').type(first_answer_variant)
        s('.survey-question:nth-child(5) .input-group:nth-child(2) .survey-question-choice').click()
        time.sleep(0.7)
        s('.survey-question:nth-child(5) .input-group:nth-child(2) .survey-question-choice').type(second_answer_variant)
        s('.survey-question:nth-child(5) .input-group:nth-child(3) .survey-question-choice').click()
        time.sleep(0.9)
        s('.survey-question:nth-child(5) .input-group:nth-child(3) .survey-question-choice')\
            .with_(timeout=7).type(third_answer_variant)
        return self

    def add_sixth_questions_type_rating(self, sixth_question_type: str):
        s('.panel-body #survey-new-question-type').click()
        s('#survey-new-question-type [value="rating"]').click()
        s('#questions-panel #survey-new-question').click()
        s('.survey-question:nth-child(6) .panel-title').should(have.text(sixth_question_type))
        time.sleep(0.7)
        return self

    def add_sixth_question_content(self, content_sixth_question: str):
        s('.survey-question:nth-child(6) .jodit-wysiwyg').type(content_sixth_question)
        return self

    def add_answers_to_sixth_question(self, first_answer_version: str, second_answer_version: str):
        s('.survey-question:nth-child(6) .survey-question-from-input').type(first_answer_version)
        time.sleep(0.9)
        s('.survey-question:nth-child(6) .survey-question-to-input').type(second_answer_version)
        s('.survey-question:nth-child(6) .survey-question-from-input').click()
        return self

    def checking_question_type_and_sequence_number(self, value):
        list_question = s('#survey-questions').with_(timeout=7)
        list_question.all('.panel-heading').element_by_its('.panel-title', have.exact_text(value))
        return self

    def adding_question_replication(self, seventh_question_type: str):
        s('.survey-question:nth-child(6) .survey-question-copy').with_(timeout=5).perform(command.js.scroll_into_view).\
            click()
        s('.survey-question:nth-child(7) .panel-title').should(have.text(seventh_question_type))
        return self

    def import_first_questions_from_another_survey(self, import_question_text: str):
        s('.panel-body #survey-import-questions-modal-open').click()
        s('[for="survey-import-title"]').with_(timeout=3).should(have.text(import_question_text))
        return self

    def search_and_choosing_first_a_survey(self, name_first_survey: str):
        s('#survey-import-modal #survey-import-questions-input').click().type(name_first_survey)
        s('[data-id="29"]').click()
        s('#survey-import-modal #survey-import-questions').click()
        return self

    def import_second_questions_from_another_survey(self, import_question_text: str):
        s('.panel-body #survey-import-questions-modal-open').with_(timeout=10).click()
        s('[for="survey-import-title"]').with_(timeout=3).should(have.text(import_question_text))
        s('#survey-import-modal #survey-import-questions-input').clear()
        return self

    def search_and_choosing_second_a_survey(self, name_second_survey: str):
        s('#survey-import-modal #survey-import-questions-input').type(name_second_survey).press_enter()
        s('[data-id="99"]').with_(timeout=5).click()
        s('#survey-import-modal #survey-import-questions').click()
        return self

    def open_created_survey(self, name_survey: str):
        s('#survey-filter-title').type(name_survey).press_enter()
        s('.admin-list .survey_title').with_(timeout=20).should(have.text(name_survey))
        s('.admin-list .survey_edit').click()
        return self

    def open_questions_block(self):
        s('[data-target="#questions-panel"] .fa-plus').with_(timeout=5).click()
        return self

    def delete_one_question(self):
        s('.survey-question:nth-child(7) .panel-heading .fa-trash').perform(command.js.scroll_into_view).click()
        s('.container .btn-default:nth-child(1)').click()
        return self

    def checking_the_display_push_message(self, value):
        s('[data-notify="message"]').with_(timeout=5).should(have.text(value))
        time.sleep(2)
        return self

    def change_survey_name(self):
        s('[data-target="#general-panel"] .fa-plus').with_(timeout=5).click()
        s('#survey-title').clear().type(' ')
        return self
