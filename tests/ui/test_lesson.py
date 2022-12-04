from allure import title, tag, step
from diploma_project_tests.model.authorization import authorization_on_admin_panel
from diploma_project_tests.helpers import app
from diploma_project_tests.data.data import *


@tag("Web UI")
@title("Creating a lesson")
def test_add_lesson(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the lessons page"):
        app.lesson_page.open_lessons_page('Lessons')

    with step("Creating a lesson"):
        app.lesson_page.creat_a_lesson()

        with step("Checking the Adding Lesson page display"):
            app.lesson_page.checking_lesson_page_title('Adding Lesson')

        with step("Changing the status to active to display on the site"):
            app.lesson_page.chang_status()

        with step("Choose a category"):
            app.lesson_page.add_category()

        with step("Adding price"):
            app.lesson_page.add_price(Lessons.normal_price, Lessons.discount_price)

        with step("Filling in the Lesson Details"):
            with step("Filling in the title"):
                app.lesson_page.add_title(Lessons.title_lesson)

            with step("Filling content of lesson"):
                app.lesson_page.add_description(Lessons.description_text)

    with step("Submit the form"):
        app.lesson_page.submit_form()


@tag("Web UI")
@title("Filling the lesson with information")
def test_filling_the_lesson(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the lessons page"):
        app.lesson_page.open_lessons_page('Lessons')

    with step("Search for the created lesson and open it"):
        app.lesson_page.search_created_lesson(Lessons.title_lesson, Lessons.name_lesson)

    with step("Checking the Adding Lesson page display"):
        app.lesson_page.checking_lesson_page_title('Editing Lesson')

        with step("Specifying the 'Show date edited' checkbox"):
            app.lesson_page.show_date_edited()

        with step("Adding files"):
            app.lesson_page.add_files(Lessons.document, Lessons.table)

        with step("Adding lecturer"):
            app.lesson_page.add_lecturer(Lessons.name_lecturer)

        with step("Adding part of lesson"):
            with step("Adding Part #1"):
                app.lesson_page.add_first_part_of_lesson()

                with step("Filling in the title"):
                    app.lesson_page.add_title_first_part(Lessons.title_first_part_lesson)

                with step("Adding video"):
                    app.lesson_page.add_video_first_part(Lessons.video_first_part_lesson)

                with step("Mark indications 'Speech from a summary'"):
                    with step("Specifying the 'Text to Speech' checkbox"):
                        app.lesson_page.text_to_speech()

                    with step("Mark indications 'Don't show the About text'"):
                        app.lesson_page.not_show_the_about_text()

                with step("Checking the video upload"):
                    app.lesson_page.checking_the_video_upload_part_one(Lessons.text_message)

            with step("Save part lesson #1"):
                app.lesson_page.save_first_part_lesson()

            with step("Close the block part of the lesson #1"):
                app.lesson_page.close_first_part_block()

            with step("Adding part #2"):
                app.lesson_page.add_second_part_of_lesson()

                with step("Filling in the title"):
                    app.lesson_page.add_title_second_part(Lessons.title_second_part_lesson)

                with step("Adding video"):
                    app.lesson_page.add_video_second_part(Lessons.video_second_part_lesson)

                with step("Checking the video upload"):
                    app.lesson_page.checking_the_video_upload_second_part(Lessons.text_message)

            with step("Save part lesson #2"):
                app.lesson_page.save_second_part_lesson()

            with step("Close the block part of the lesson #2"):
                app.lesson_page.close_second_part_block()

        with step("Moving blocks of parts of lessons between themselves"):
            app.lesson_page.moving_blocks_of_parts()


@tag("Web UI")
@title("Deleting the lesson")
def test_deleting_the_lesson(setup_browser):
    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the lesson page"):
        app.lesson_page.open_lessons_page('Lessons')

    with step("Deleting a created lesson"):
        with step("Search for a created lesson and delete it"):
            app.lesson_page.delete_created_lesson(Lessons.title_lesson, Lessons.name_lesson)

        with step("Display a push message about successful removal of the lesson"):
            app.lesson_page.push_message_about_successful_removal_lesson('Lesson has been deleted')
