import time
from selene.support.shared import browser # убрать если нужен запуск удаленно
from yeda_admin_panel_tests.controls.utils import resource
from yeda_admin_panel_tests.pages.authorization_website import authorization_on_the_site

name_course = 'QA Automation course'

def test_create_course(setup_browser):
    # browser = setup_browser # розкамитить если нужен запуск удаленно

    authorization_on_the_site()

    browser.element('[href="/admin/courses"]').click()

    browser.element('[yedaoldadminhref="elearning/courses/create"]').click()

    browser.element('#dropdownMenuButton').click()
    browser.element('[data-status-id="3"]').click()

    browser.element('#dropdown-category').click()
    browser.element('[data-category-id="115"]').click()  # QA

    browser.element('#name').type(f'{name_course}')

    browser.element('#generate-slug').click()
    # browser.element('#slug').should(have.exact_texts('qa-automation-course'))

    browser.element('[name="short_descr"]').type('This course about how to learn QA Automation')

    browser.element('[name="descr"]').type('This course about how to learn QA Automation')

    browser.element('[name="duration"]').type('12 month')

    browser.element('[name="prerequisites"]').type('Not have')

    browser.element('[name="video_link"]').type('https://vimeo.com/437087249')  # Video or image

    browser.element('#course_photo').send_keys(resource('circle.png'))  # Teaser images

    browser.element('[name="meta_title"]').type('QA Automation')  # Search Engine Optimization
    browser.element('[name="meta_description"]').type('This course about how to learn QA Automation')
    browser.element('[name="meta_author"]').type('QA')

    browser.element('#date_begin_date').type('2023-01-01').press_tab()

    browser.element('#date_end_date').type('2023-02-28').press_tab()

    browser.element('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
    browser.element('.jodit-wysiwyg').type('QA Automation').press_enter()
    browser.element('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
    browser.element('.jodit-wysiwyg').type('This course about how to learn QA').press_enter()

    browser.element('[name="show_files_to_students"]').click()

    browser.element('[name="normal_price"]').type('100')
    browser.element('[name="discount_price"]').type('60')

    browser.element('[type="submit"]').click()
    time.sleep(3)


 #добавить файлы при создании курса
 #проверить что курс создан