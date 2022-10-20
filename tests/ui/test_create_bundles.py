import time
from selene import have, command

from selene.support.shared import browser

from yeda_admin_panel_tests.controls.utils import resource
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel

name_bundle = 'QA Bundle'


def test_create_bundle(setup_browser):
    # browser = setup_browser

    authorization_on_admin_panel()

    browser.element('[href="https://dev.biflow.co/collegeadmin/elearning/bundles"]').click()

    browser.element('.page-header').should(have.text('Bundles'))

    browser.element('.btn.btn-primary').click()

    browser.element('.page-header').should(have.text('Adding Bundle'))

    browser.element('#name').type(f'{name_bundle}')

    browser.element('[name="duration"]').type('12 months')

    browser.element('[name="prerequisites"]').type('no limits')

    browser.element('[name="video_link"]').type('https://vimeo.com/437087249')

    browser.element('[name="description"]').type('This bundle about how to learn QA')

    # browser.element('.jodit-workplace').type('')
    browser.element('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
    browser.element('.jodit-wysiwyg').type('QA Automation').press_enter()
    browser.element('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
    browser.element('.jodit-wysiwyg').type('This course about how to learn QA').press_enter()

    browser.element('#bundle_files_input').send_keys(resource('circle.png'))
    browser.element('#bundle_files_input').send_keys(resource('QA.mp4'))

    browser.element('#status-bundle-dropdown').click()
    browser.element('[data-status-id="3"]').click()

    browser.element('.panel-body .checkbox.col-12.w-100 [value="10"]').click()
    browser.element('.panel-body .checkbox.col-12.w-100 [value="115"]').click()

    browser.element('.image_upload_bundle').send_keys(resource('circle.png'))

    browser.element('[name="seo[meta_title]"]').type('QA Bundle Automation')  # Search Engine Optimization
    browser.element('[name="seo[meta_description]"]').type('This bundle about how to learn Automation')
    browser.element('#bundle-generate-slug').click()

    browser.element('#date_begin_date').type('2023-02-01').press_tab()

    browser.element('#date_end_date').type('2023-02-26').press_tab()

    browser.element('[name="price"]').type('150')
    browser.element('[name="discount_price"]').type('80')

    browser.element('[type="submit"]').click()

    browser.element('.page-header').with_(timeout=20).should(have.text('Editing Bundle'))

