import time
import lorem
import os

from dotenv import load_dotenv
from selene import have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from diploma_project_tests.controls.utils import resource


class CreateArticle:

    def open_settings_page(self, value):
        s('#portal-header-default').with_(timeout=5).should(have.text(value))  # הגדרות
        return self

    def open_articles_page(self):
        s('[href="/admin/articles/main"').click()
        return self

    def checking_the_display_of_the_articles_page(self, value):
        s('#portal-header-default').with_(timeout=6).should(have.text(value))  # מאמרים
        time.sleep(4)
        return self

    def create_article(self):
        s('//button[text() = "Add New Article"]').click()  # מאמר חדש
        time.sleep(2)
        return self

    def checking_new_article_page(self, value):
        s('//div[text() = "New Article"]').with_(timeout=7).should(have.text(value))
        s('.air-h1.center.title').click()
        return self

    def add_title(self):
        NAME_ARTICLE = os.getenv('name_article')
        s('.title-editable.air-input').clear().type(f'{NAME_ARTICLE}')
        return self

    def deleting_default_text(self):
        s('#text-content').click()
        s('.ck-editor__main .ck-editor__editable').click()
        s('[data-placeholder="Enter text here"]').clear()  # הכנס טקסט
        s('.ck-alignment-dropdown > button').click()
        s('.ck-toolbar_vertical.ck-toolbar .ck-toolbar__items button:nth-child(3)').click()
        s('.ck-sticky-panel__content > div > div > button:nth-child(3)').click()
        return self

    def add_content_to_article(self, context_text: str):
        article_content = lorem.paragraph()
        s('.ck-editor__main .ck-editor__editable').type(article_content).press_enter()
        s('.ck-editor__main .ck-editor__editable').type(context_text).press_enter()
        return self

    def add_video(self, video_link: str):
        s('div:nth-child(26) > button').click()
        s('.ck-labeled-field-view__input-wrapper .ck-input').type(video_link)
        s('.ck-dropdown__panel .ck-button-save').click()
        return self

    def add_image(self, picture: str):
        s('.avatar-wrapper [type="file"]').send_keys(resource(picture))
        time.sleep(4)
        return self

    def publish_article(self):
        s('#publish').click()
        return self

    def generate_slug_id(self):
        s('.control .air-button').click()
        return self

    def add_seo(self, seo_author: str):
        seo_title = lorem.sentence()
        seo_description = lorem.sentence()
        seo_keywords = lorem.sentence()
        s('#seo_title').clear().type(seo_title)
        s('#description').type(seo_description)
        s('#keywords').type(seo_keywords).press_enter()
        s('#author').type(seo_author).press_enter()
        time.sleep(2)
        return self

    def go_to_settings_page(self, value):
        s('#to-admin-button').with_(timeout=8).click()
        s('#portal-header-default').with_(timeout=5).should(have.text(value))  # הגדרות Settings
        s('[href="/admin/articles/main"').click()
        return self

    def go_to_articles_page(self, value):
        s('#portal-header-default').with_(timeout=6).should(have.text(value))  # Articles מאמרים
        return self

    def refreshing_the_page(self):
        browser.driver().refresh()
        time.sleep(5)
        return self

    def search_created_article_and_delete(self):
        NAME_ARTICLE = os.getenv('name_article')
        table = browser.element('.cdk-table')
        table.all('.cdk-row').element_by_its('.cdk-column-menu_name', have.exact_text(f'{NAME_ARTICLE}'))\
            .element('.cdk-column-delete').click()
        time.sleep(1)
        return self
