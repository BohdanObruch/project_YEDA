import time
import lorem

from selene import have, command
from selene.support.shared import browser
from yeda_admin_panel_tests.pages.authorization_website import authorization_on_the_site
from yeda_admin_panel_tests.controls.utils import resource
from allure import title, tag, step


@tag("Web UI")
@title("Creating an article and filling it with information")
def test_add_article(setup_browser):
    # browser = setup_browser
    name_article = lorem.sentence()
    article_content = lorem.paragraph()

    with step("Authorization on the site and go to the admin panel"):
        authorization_on_the_site()

    with step("Checking that the Settings page has opened"):
        browser.element('#portal-header-default').with_(timeout=5).should(have.text('Settings'))  # הגדרות

    with step("Go to articles page"):
        browser.element('[href="/admin/articles/main"').click()

    with step("Checking that the Articles page has opened"):
        browser.element('#portal-header-default').with_(timeout=6).should(have.text('Articles'))  # מאמרים
        time.sleep(2)

        with step("Click on the create article button"):
            browser.element('//button[text() = "Add New Article"]').click()  # מאמר חדש
            time.sleep(2)

    with step("Checking that the New Article page has opened"):
        browser.element('//div[text() = "New Article"]').with_(timeout=7).should(have.text('New Article'))
        browser.element('.air-h1.center.title').click()

        with step("Filling in the title of the article"):
            browser.element('.title-editable.air-input').clear().type(f'{name_article}')

        with step("Preparing and deleting default text in a field"):
            browser.element('#text-content').click()
            browser.element('.ck-editor__main .ck-editor__editable').click()
            browser.element('[data-placeholder="Enter text here"]').clear()  # הכנס טקסט
            browser.element('.ck-alignment-dropdown > button').click()
            browser.element('.ck-toolbar_vertical.ck-toolbar .ck-toolbar__items button:nth-child(3)').click()
            browser.element('.ck-sticky-panel__content > div > div > button:nth-child(3)').click()

        with step("Filling in the content of the article"):
            browser.element('.ck-editor__main .ck-editor__editable').type(article_content).press_enter()
            browser.element('.ck-editor__main .ck-editor__editable').type('Good luck!').press_enter()

        with step("Adding a video to an article"):
            browser.element('div:nth-child(26) > button').click()
            browser.element('.ck-labeled-field-view__input-wrapper .ck-input').type('https://vimeo.com/53801675')
            browser.element('.ck-dropdown__panel .ck-button-save').click()

        with step("Adding a picture to an article"):
            browser.element('.avatar-wrapper [type="file"]').send_keys(resource('circle.png'))
            time.sleep(4)

        with step("Displaying an article on the site"):
            browser.element('#publish').click()

        with step("Slug ID generation"):
            browser.element('.control .air-button').click()

        with step("Filling the SEO Block"):
            with step("Filling Title"):
                browser.element('#seo_title').clear().type(name_article)

            with step("Filling Description"):
                browser.element('#description').type(name_article)

            with step("Filling Keywords"):
                browser.element('#keywords').type(name_article).press_enter()

            with step("Filling Author"):
                browser.element('#author').type('QA').press_enter()
                time.sleep(2)

    with step("Deleting a created article"):
        browser.element('#to-admin-button').with_(timeout=8).click()

        with step("Go to the admin panel to the page with settings"):
            browser.element('#portal-header-default').with_(timeout=5).should(have.text('Settings'))  # הגדרות Settings
            browser.element('[href="/admin/articles/main"').click()

        with step("Go to the Articles page"):
            browser.element('#portal-header-default').with_(timeout=6).should(have.text('Articles'))  # Articles מאמרים

        with step("Refreshing the page to display the created article"):
            browser.driver().refresh()
            time.sleep(5)

        with step("Search and delete the created article"):
            table = browser.element('.cdk-table')
            table.all('.cdk-row').element_by_its('.cdk-column-menu_name', have.exact_text(f'{name_article}')) \
                .element('.cdk-column-delete').click()
            time.sleep(1)
