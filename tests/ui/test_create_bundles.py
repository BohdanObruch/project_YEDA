from selene import have
from selene.support.shared import browser
from yeda_admin_panel_tests.controls.utils import resource
from yeda_admin_panel_tests.model.authorization import authorization_on_admin_panel
from allure import title, tag, step
from yeda_admin_panel_tests.helpers import app
from yeda_admin_panel_tests.data.data import *


@tag("Web UI")
@title("Creating an bundle")
def test_create_bundle(setup_browser):
    # browser = setup_browser

    with step("Authorization on the admin panel"):
        authorization_on_admin_panel()

    with step("Go to the bundle page"):
        app.create_bundles.open_bundles_page('Bundles')

    with step("Checking the Adding Bundle page display"):
        app.create_bundles.checking_adding_bundle_page('Adding Bundle')

    with step("Creating a bundle"):
        with step("Filling in the title"):
            app.create_bundles.add_title()

        with step("Filling in the duration"):
            app.create_bundles.add_duration(Bundles.duration)

        with step("Filling in the prerequisites"):
            app.create_bundles.add_prerequisites(Bundles.prerequisites)

        with step("Adding video"):
            app.create_bundles.add_video(Bundles.video_link)

        with step("Filling a short description"):
            app.create_bundles.add_short_description(Bundles.short_descriptoin)

        with step("Filling a description"):
            app.create_bundles.add_description(Bundles.description_line1, Bundles.description_line2)

        with step("Adding associated files"):
            app.create_bundles.add_associated_files(Bundles.picture, Bundles.video)

        with step("Changing status to active"):
            app.create_bundles.change_status()

        with step("Adding categories"):
            app.create_bundles.add_category()

        with step("Adding teaser images"):
            app.create_bundles.add_teaser_image(Bundles.picture)

        with step("Adding SEO"):
            app.create_bundles.add_seo(Bundles.seo_title, Bundles.seo_description)

        with step("Adding start date"):
            app.create_bundles.add_start_date(Bundles.start_date)

        with step("Adding end date"):
            app.create_bundles.add_end_date(Bundles.end_date)

        with step("Adding price"):
            app.create_bundles.add_price(Bundles.normal_price, Bundles.discount_price)

    with step("Submit the form"):
        app.create_bundles.submit_form()

    with step("Checking page title changes on the Editing Bundle"):
        app.create_bundles.check_page_title('Editing Bundle')
