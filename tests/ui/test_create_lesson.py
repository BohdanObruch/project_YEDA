from selene.support.shared import browser
from yeda_admin_panel_tests.controls.utils import resource
from allure import title, tag, step
from yeda_admin_panel_tests.model.authorization import authorization_on_admin_panel
from yeda_admin_panel_tests.helpers import app
from yeda_admin_panel_tests.data.data import *


@tag("Web UI")
@title("Creating an lesson and filling it with information")
def test_add_lesson(setup_browser):
    # browser = setup_browser

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the lesson page"):
        app.create_lesson.open_lessons_page('Lessons')

    with step("Creating a lesson"):
        app.create_lesson.creat_a_lesson()

        with step("Checking the Adding Lesson page display"):
            app.create_lesson.checking_adding_lesson_page('Adding Lesson')

        with step("Changing the status to active to display on the site"):
            app.create_lesson.chang_status()

        with step("Choose a category"):
            app.create_lesson.add_category()

        with step("Adding price"):
            app.create_lesson.add_price(Lessons.normal_price, Lessons.discount_price)

        with step("Filling in the Lesson Details"):
            with step("Filling in the title"):
                app.create_lesson.add_title(Lessons.title_lesson)

            with step("Filling content of lesson"):
                app.create_lesson.add_description(Lessons.description_text)

    with step("Submit the form"):
        app.create_lesson.submit_form()

        with step("Specifying the 'Show date edited' checkbox"):
            app.create_lesson.show_date_edited()

        with step("Adding files"):
            app.create_lesson.add_files(Lessons.document, Lessons.table)

    with step("Editing lesson"):
        with step("Adding lecturer"):
            app.create_lesson.add_lecturer(Lessons.name_lecturer)

        with step("Adding part of lesson"):
            with step("Adding Part #1"):
                app.create_lesson.add_first_part_of_lesson()

                with step("Filling in the title"):
                    app.create_lesson.add_title_first_part(Lessons.title_first_part_lesson)

                with step("Adding video"):
                    app.create_lesson.add_video_first_part(Lessons.video_first_part_lesson)

                with step("Mark indications 'Speech from a summary'"):
                    with step("Specifying the 'Text to Speech' checkbox"):
                        app.create_lesson.text_to_speech()

                    with step("Mark indications 'Don't show the About text'"):
                        app.create_lesson.not_show_the_about_text()

                with step("Checking the video upload"):
                    app.create_lesson.checking_the_video_upload_part_one(Lessons.text_message)

            with step("Save part lesson #1"):
                app.create_lesson.save_first_part_lesson()

            with step("Close the block part of the lesson #1"):
                app.create_lesson.close_first_part_block()

            with step("Adding part #2"):
                app.create_lesson.add_second_part_of_lesson()

                with step("Filling in the title"):
                    app.create_lesson.add_title_second_part(Lessons.title_second_part_lesson)

                with step("Adding video"):
                    app.create_lesson.add_video_second_part(Lessons.video_second_part_lesson)

                with step("Checking the video upload"):
                    app.create_lesson.checking_the_video_upload_second_part(Lessons.text_message)

            with step("Save part lesson #2"):
                app.create_lesson.save_second_part_lesson()

            with step("Close the block part of the lesson #2"):
                app.create_lesson.close_second_part_block()

        with step("Moving blocks of parts of lessons between themselves"):
            app.create_lesson.moving_blocks_of_parts()

        with step("Deleting a created lesson"):
            with step("Go to the Lessons page"):
                app.create_lesson.open_all_lessons_page()

            with step("Search for a created lesson and delete it"):
                app.create_lesson.search_created_lesson_and_delete(Lessons.title_lesson, Lessons.name_lesson)

            with step("Display a push message about successful removal of the lesson"):
                app.create_lesson.push_message_about_successful_removal_lesson('Lesson has been deleted')
