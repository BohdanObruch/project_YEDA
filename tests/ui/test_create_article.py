from allure import title, tag, step
from diploma_project_tests.model.authorization import authorization_on_the_site
from diploma_project_tests.helpers import app
from diploma_project_tests.data.data import *


@tag("Web UI")
@title("Creating an article and filling it with information")
def test_add_article(setup_browser):
    browser = setup_browser

    with step("Authorization on the site and go to the admin panel"):
        authorization_on_the_site()

    with step("Checking that the Settings page has opened"):
        app.create_article.open_settings_page('Settings')

    with step("Go to articles page"):
        app.create_article.open_articles_page()

    with step("Checking that the Articles page has opened"):
        app.create_article.checking_the_display_of_the_articles_page('Articles')

        with step("Click on the create article button"):
            app.create_article.create_article()

    with step("Checking that the New Article page has opened"):
        app.create_article.checking_new_article_page('New Article')

        with step("Filling in the title of the article"):
            app.create_article.add_title()

        with step("Preparing and deleting default text in a field"):
            app.create_article.deleting_default_text()

        with step("Filling in the content of the article"):
            app.create_article.add_content_to_article(Article.context_text)

        with step("Adding a video to an article"):
            app.create_article.add_video(Article.video_link)

        with step("Adding a picture to an article"):
            app.create_article.add_image(Article.picture)

        with step("Displaying an article on the site"):
            app.create_article.publish_article()

        with step("Slug ID generation"):
            app.create_article.generate_slug_id()

        with step("Filling the SEO Block"):
            with step("Filling Title,Description,Keywords,Author"):
                app.create_article.add_seo(Article.seo_author)

    with step("Deleting a created article"):
        with step("Go to the admin panel to the page with settings"):
            app.create_article.go_to_settings_page('Settings')

        with step("Go to the Articles page"):
            app.create_article.go_to_articles_page('Articles')

        with step("Refreshing the page to display the created article"):
            app.create_article.refreshing_the_page()

        with step("Search and delete the created article"):
            app.create_article.search_created_article_and_delete()
