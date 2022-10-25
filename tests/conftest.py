import requests
import os
import pytest
import json
import calendar
import time
import datetime as DT

from datetime import date
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from yeda_admin_panel_tests.controls import attach
from yeda_admin_panel_tests.utils.sessions import yeda
from yeda_admin_panel_tests.controls.utils import resource
from appium import webdriver
from yeda_admin_panel_tests.utils import attachment


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


WEB_URL = os.getenv('url_yeda_website')
ADMIN_PANEL_URL = os.getenv('url_yeda_admin_panel')
ID_COLLEGE = os.getenv('id_college')


@pytest.fixture(scope='function')
def setup_browser():
    browser.config.base_url = WEB_URL
    browser.config.window_width = 1920
    browser.config.window_height = 1920
    yield
    browser.quit()


# @pytest.fixture(scope='function', autouse=True)
# def browser_management():
#     browser.config.base_url = os.getenv('selene.base_url', WEB_URL)
#     browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
#     browser.config.hold_browser_open = (
#             os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
#     )
#     browser.config.timeout = float(os.getenv('selene.timeout', '3'))
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#
#
# DEFAULT_BROWSER_VERSION = "103.0"
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_version',
#         default='103.0'
#     )


#
# @pytest.fixture(scope='function')
# def setup_browser(request):
#     browser_version = request.config.getoption('--browser_version')
#     browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": browser_version,
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#
#     url = os.getenv('URL')
#
#     driver = webdriver.Remote(
#         command_executor=f"{url}/wd/hub",
#         options=options
#     )
#     browser.config.driver = driver
#     yield browser
#
#     attach.add_html(browser)
#     attach.add_logs(browser)
#     attach.add_screenshot(browser)
#     attach.add_video(browser)


def opened_page_website():
    browser.open(WEB_URL)


def opened_page_admin_panel():
    browser.open(ADMIN_PANEL_URL)
    browser.config.driver.maximize_window()


@pytest.fixture()  # scope='session', autouse=True
def register_user():
    now = DT.datetime.now(DT.timezone.utc).astimezone()
    time_format = "%Y-%m-%d %H:%M:%S"
    now_time = f"{now:{time_format}}"

    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    name = ('anna' + str(ts))
    email = (name + '@gmail.com')
    password = ts

    user = {
        "email": f"{email}",
        "password": f"{password}",
        "lang": "en",
        "college_id": ID_COLLEGE,
        "signed": f"{now_time}"
    }

    current_college_id = f'current_college_id={ID_COLLEGE}'

    response = yeda().post('/auth/register',
                           params=current_college_id,
                           data=user
                           )

    response_parse = json.loads(str(response.text))

    token = response_parse['auth']['access_token']
    user_name = response_parse["user"]["name"]
    user_email = response_parse["user"]["email"]
    user_pass = ts
    id = response_parse["user"]["id"]

    return token, user_name, user_email, user_pass, id


@pytest.fixture(scope='function')  # (scope='function', autouse=True)
def setup():
    desired_capabilities = ({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Samsung Galaxy S20",
        "os_version": "10.0",
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "build": "browserstack-build-" + str(date.today()),
        'bstack:options': {
            "sessionName": "Python project test",
            "projectName": "Python project",
        }
    })

    userName = os.getenv('LOGIN')
    accessKey = os.getenv('KEY')
    remoteUrl = os.getenv('APPIUM_BROWSERSTACK')
    browser.config.driver = webdriver.Remote(f"http://{userName}:{accessKey}@{remoteUrl}/wd/hub", desired_capabilities)
    browser.config.timeout = 4
    session_id = browser.config.driver.session_id

    yield

    browser.quit()
    attachment.add_video(session_id, 'Test video')
