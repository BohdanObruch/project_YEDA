from selene.support.shared import browser  # убрать если нужен запуск удаленно
from allure import title, tag, step
from diploma_project_tests.model.authorization import authorization_on_the_site
from diploma_project_tests.helpers import app
from diploma_project_tests.data.data import *


@tag("Web UI")
@title("Creating an course")
def test_create_course(setup_browser):
    # browser = setup_browser # розкамитить если нужен запуск удаленно

    with step("Authorization on the site and go to the admin panel"):
        authorization_on_the_site()

    with step("Go to the courses page"):
        app.create_course.open_courses_page()

    with step("Creating a course"):
        app.create_course.creat_course()

        with step("Changing the status to active to display on the site"):
            app.create_course.change_status()

        with step("Choose a category"):
            app.create_course.add_category()

        with step("Filling in the name of the course"):
            app.create_course.add_title()

        with step("Generate slug"):
            app.create_course.add_slug()

        with step("Filling in the short description"):
            app.create_course.add_short_description(Course.short_description)

        with step("Adding a description"):
            app.create_course.add_description(Course.description)

        with step("Filling in the duration"):
            app.create_course.add_duration(Course.duration)

        with step("Filling in the prerequisites"):
            app.create_course.add_prerequisites(Course.prerequisites)

        with step("Adding video to the 'Video or image' block"):
            app.create_course.add_video('https://vimeo.com/437087249')

        with step("Adding teaser images"):
            app.create_course.add_teaser_image(Course.picture)

        with step("Adding description"):
            app.create_course.add_about_course(Course.description_line1, Course.description_line2)

        with step("Associated files"):
            with step("Displaying files only for students of the course and adding"):
                app.create_course.add_associated_files(Course.file, Course.table)

        with step("Adding SEO"):
            with step("Filling Title, Description, Author"):
                app.create_course.add_seo(Course.seo_title, Course.seo_description, Course.seo_author)

        with step("Adding start date"):
            app.create_course.add_start_date(Course.start_date)

        with step("Adding end date"):
            app.create_course.add_end_date(Course.end_date)

        with step("Adding price"):
            app.create_course.add_price(Course.normal_price, Course.discount_price)

    with step("Submit the form"):
        app.create_course.submit_form()

    with step("Checking page title changes on the Editing Course"):
        app.create_course.check_page_title('Editing Course')

    with step("Deleting a created Course"):
        with step("Go to the page with all the courses"):
            app.create_course.open_all_courses_page('Courses')

        with step("Search for a created course and delete it"):
            app.create_course.search_created_course_and_delete()

        with step("Checking that the created course has been deleted"):
            app.create_course.checking_that_the_course_has_been_deleted()
