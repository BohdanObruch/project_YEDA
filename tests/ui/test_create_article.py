import time

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_website import authorization_on_the_site
from yeda_admin_panel_tests.controls.utils import resource

name_article = 'Abbreviated reading in a time limit'


def test_add_article(setup_browser):
    # browser = setup_browser

    authorization_on_the_site()

    browser.element('#portal-header-default').with_(timeout=5).should(have.text('Settings'))# הגדרות

    browser.element('[href="/admin/articles/main"').click()

    browser.element('#portal-header-default').with_(timeout=6).should(have.text('Articles'))# מאמרים
    time.sleep(2)
    browser.element('//button[text() = "Add New Article"]').click() # מאמר חדש
    time.sleep(2)

    # Add new article
    browser.element('//div[text() = "New Article"]').with_(timeout=7).should(have.text('New Article'))
    browser.element('.air-h1.center.title').click()

    browser.element('.title-editable.air-input').clear().type(f'{name_article}')
    browser.element('#text-content').click()
    browser.element('.ck-editor__main .ck-editor__editable').click()
    browser.element('[data-placeholder="Enter text here"]').clear() # הכנס טקסט
    browser.element('.ck-alignment-dropdown > button').click()
    browser.element('.ck-toolbar_vertical.ck-toolbar .ck-toolbar__items button:nth-child(3)').click()
    browser.element('.ck-sticky-panel__content > div > div > button:nth-child(3)').click()
    browser.element('.ck-editor__main .ck-editor__editable').type(' Reading improvement This is the most '
                                                                  'critical part you need to focus on while '
                                                                  'you are under a time limit on the exam.').press_enter()
    browser.element('.ck-editor__main .ck-editor__editable').type("There's a video for that, which explains how you "
                                                                  "can maximize your reading when you're short on "
                                                                  "time.").press_enter()
    browser.element('.ck-editor__main .ck-editor__editable').type('Good luck!').press_enter()
    browser.element('div:nth-child(26) > button').click()
    browser.element('.ck-labeled-field-view__input-wrapper .ck-input').type('https://vimeo.com/53801675')
    browser.element('.ck-dropdown__panel .ck-button-save').click()

    # add picture
    browser.element('.avatar-wrapper [type="file"]').send_keys(resource('circle.png'))
    time.sleep(4)

    # publish
    browser.element('#publish').click()

    # slug
    browser.element('.control .air-button').click()

    # SEO
    # Title
    browser.element('#seo_title').clear().type(f'{name_article}')

    # Description
    browser.element('#description').type('Verbal chapter improvement')

    # Keywords
    browser.element('#keywords').type('Abbreviated reading').press_enter()

    # Author
    browser.element('#author').type('QA').press_enter()
    time.sleep(2)

    # Delete
    browser.element('#to-admin-button').with_(timeout=8).click()

    browser.element('#portal-header-default').with_(timeout=5).should(have.text('Settings'))  # הגדרות Settings

    browser.element('[href="/admin/articles/main"').click()

    browser.element('#portal-header-default').with_(timeout=6).should(have.text('Articles'))#Articles מאמרים

    browser.driver().refresh()
    time.sleep(5)

    table = browser.element('.cdk-table')
    table.all('.cdk-row').element_by_its('.cdk-column-menu_name', have.exact_text(f'{name_article}'))\
        .element('.cdk-column-delete').click()
    time.sleep(1)
