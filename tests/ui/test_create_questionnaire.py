import time

from selene import have
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from yeda_admin_panel_tests.controls.utils import resource

name_questionnaire = 'The provider - practice before the course'


def test_create_questionnaire(setup_browser):
    # browser = setup_browser

    authorization_on_admin_panel()

    browser.element('.elearning-nav-li').click()
    browser.element('.questionnaires-nav-li').click()

    browser.element('.page-header').with_(timeout=4).should(have.text('Questionnaires'))

    browser.element('.panel-heading .btn').click()

    browser.element('.page-header').with_(timeout=4).should(have.text('Adding Questionnaire'))

    browser.element('#dropdownMenuButton').click()
    browser.element('[data-status-id="3"]').click()

    browser.element('#dropdown-category').click()
    browser.element('[data-category-id="115"]').click()  # QA

    browser.element('#title').type(f'{name_questionnaire}')

    browser.element('[name="short_descr"]').type('Here is a matriculation in English model E. This matriculation is '
                                                 'for practice only, so you can take your time and solve it slowly '
                                                 'and thoroughly. Successfully!')

    browser.element('.jodit-workplace .jodit-wysiwyg').type(' ')
    browser.element('.jodit-ui-group_group_indent .jodit-toolbar-button__trigger').click()
    browser.element('.jodit-toolbar-button_center .jodit-toolbar-button__button').click()
    browser.element('.jodit-workplace .jodit-wysiwyg').type('The above exercises are designed to reset/find '
                                                            'theoretical gaps in your study process.').press_enter()

    browser.element('.jodit-ui-group_size_middle .jodit-icon_select_all').click()  # .jodit-xpath__item
    browser.element('.jodit-toolbar-button_bold').click()

    browser.element('.jodit-workplace .jodit-wysiwyg').click()
    browser.element('.jodit-workplace .jodit-wysiwyg').type(' ').press_enter()

    browser.element('.jodit-ui-group__image').click()
    browser.element('[type="file"]').send_keys(resource('mathematics.jpg'))
    browser.element('.jodit-wysiwyg img').with_(timeout=15).click()
    browser.element('.jodit-toolbar-button_pencil').click()
    browser.element('.imageHeight').clear().type('400')
    time.sleep(1)
    browser.element('.jodit-dialog__footer .jodit-ui-button_ok').click()

    browser.element('.d-inline-block [name="shuffle_questions"]').click()
    browser.element('.max-q-count [name="questions_count"').clear().type('3')

    browser.element('[type="submit"]').click()
    time.sleep(2)

