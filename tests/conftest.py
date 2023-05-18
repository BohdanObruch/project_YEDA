import os
import pytest
import json

from datetime import date
from diploma_project_tests.utils.sessions import yeda
from appium import webdriver
from selene.support.shared import browser
from selenium import webdriver as webdriver_selenium
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values, load_dotenv
from diploma_project_tests.controls import attach
from diploma_project_tests.utils.requests_helper import user_api


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


dotenv = dotenv_values()

web_url = dotenv.get('WEB_URL')
admin_panel_url = dotenv.get('ADMIN_PANEL_URL')
id_college = dotenv.get('ID_COLLEGE')


def opened_page_website():
    browser.open(web_url)


def opened_page_admin_panel():
    browser.open(admin_panel_url)
    browser.config.driver.maximize_window()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', web_url)
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.window_width = 1920
    browser.config.window_height = 1080


DEFAULT_BROWSER_VERSION = "110.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='110.0'
    )


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    url = os.getenv('URL')

    driver = webdriver_selenium.Remote(
        command_executor=f"{url}/wd/hub",
        options=options
    )
    browser.config.driver = driver
    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video_selenoid(browser)
    browser.quit()


@pytest.fixture()
def register_user():
    data = user_api.create_user()
    current_college_id = f'current_college_id={id_college}'

    response = yeda().post('/auth/register',
                           params=current_college_id,
                           data=data
                           )

    response_parse = json.loads(str(response.text))

    token = response_parse['auth']['access_token']
    user_name = response_parse["user"]["name"]
    user_email = response_parse["user"]["email"]
    user_pass = data["password"]
    id = response_parse["user"]["id"]

    return token, user_name, user_email, user_pass, id


@pytest.fixture(scope='function')
def setup():
    linkApp = os.getenv('LINK_APP')

    desired_capabilities = ({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Samsung Galaxy S20",
        "os_version": "10.0",
        "app": f'{linkApp}',
        "build": "browserstack-build-" + str(date.today()),
        'bstack:options': {
            "sessionName": "Booking test_mobile",
            "projectName": "Booking dev",
        }
    })

    userName = os.getenv('LOGIN')
    accessKey = os.getenv('KEY')
    remoteUrl = os.getenv('APPIUM_BROWSERSTACK')
    browser.config.driver = webdriver.Remote(f"http://{userName}:{accessKey}@{remoteUrl}/wd/hub", desired_capabilities)
    browser.config.timeout = 4
    session_id = browser.config.driver.session_id

    yield

    attach.add_video(session_id, 'Test video')
    attach.screenshot(name='Last screenshot')
    attach.screen_xml_dump()

    browser.quit()
