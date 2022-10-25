import time
import pytest
import os

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.controls.utils import resource
from yeda_admin_panel_tests.pages.authorization_old_admin_panel import authorization_on_admin_panel
from allure import title, tag, step


@tag("Web UI")
@title("Creating an bundle")
def test_create_bundle(setup_browser):
    # browser = setup_browser
    NAME_BUNDLE = os.getenv('name_bundle_ui')
    URL_BUNDLES = os.getenv('url_bundles')

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the bundle page"):
        browser.element(f'[href="{URL_BUNDLES}"]').click()
        browser.element('.page-header').should(have.text('Bundles'))
        browser.element('.btn.btn-primary').click()

    with step("Checking the Adding Bundle page display"):
        browser.element('.page-header').should(have.text('Adding Bundle'))

    with step("Creating a bundle"):
        with step("Filling in the title"):
            browser.element('#name').type(f'{NAME_BUNDLE}')

        with step("Filling in the duration"):
            browser.element('[name="duration"]').type('12 months')

        with step("Filling in the prerequisites"):
            browser.element('[name="prerequisites"]').type('no limits')

        with step("Adding video"):
            browser.element('[name="video_link"]').type('https://vimeo.com/437087249')

        with step("Filling a description"):
            browser.element('[name="description"]').type('This bundle about how to learn QA')
            # browser.element('.jodit-workplace').type('')
            browser.element('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
            browser.element('.jodit-wysiwyg').type('QA Automation').press_enter()
            browser.element('.jodit-toolbar-button.jodit-toolbar-button_size_middle.jodit-toolbar-button_bold').click()
            browser.element('.jodit-wysiwyg').type('This course about how to learn QA').press_enter()

        with step("Adding associated files"):
            browser.element('#bundle_files_input').send_keys(resource('circle.png'))
            browser.element('#bundle_files_input').send_keys(resource('QA.mp4'))

        with step("Changing status to active"):
            browser.element('#status-bundle-dropdown').click()
            browser.element('[data-status-id="3"]').click()

        with step("Adding categories"):
            browser.element('.panel-body .checkbox.col-12.w-100 [value="10"]').click()
            browser.element('.panel-body .checkbox.col-12.w-100 [value="115"]').click()

        with step("Adding teaser images"):
            browser.element('.image_upload_bundle').send_keys(resource('circle.png'))

        with step("Adding SEO"):
            browser.element('[name="seo[meta_title]"]').type('QA Bundle Automation')
            browser.element('[name="seo[meta_description]"]').type('This bundle about how to learn Automation')
            browser.element('#bundle-generate-slug').click()

        with step("Adding start date"):
            browser.element('#date_begin_date').type('2023-02-01').press_tab()

        with step("Adding end date"):
            browser.element('#date_end_date').type('2023-02-26').press_tab()

        with step("Adding price"):
            browser.element('[name="price"]').type('150')
            browser.element('[name="discount_price"]').type('80')

    with step("Submit the form"):
        browser.element('[type="submit"]').click()

    with step("Checking page title changes on the Editing Bundle"):
        browser.element('.page-header').with_(timeout=20).should(have.text('Editing Bundle'))
