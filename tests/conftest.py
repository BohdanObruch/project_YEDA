import requests
import os
import pytest
import json
import calendar
import time
import datetime as DT

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from yeda_admin_panel_tests.controls import attach
from yeda_admin_panel_tests.utils.sessions import yeda


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


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


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


now = DT.datetime.now(DT.timezone.utc).astimezone()
time_format = "%Y-%m-%d %H:%M:%S"
now_time = f"{now:{time_format}}"

current_GMT = time.gmtime()
ts = calendar.timegm(current_GMT)

name = ('anna' + str(ts))
email = (name + '@gmail.com')
password = ts


@pytest.fixture()  # scope='session', autouse=True
def register_user():

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

    # response = requests.post(
    #     'https://dev.biflow.co/api/auth/register',
    #     params=current_college_id,
    #     data=user
    # )

    response_parse = json.loads(response.text)
    # token = response_parse['auth']['access_token']

    token = response_parse['auth']['access_token']

    user_name = response_parse["user"]["name"]
    user_email = response_parse["user"]["email"]
    user_pass = ts
    id = response_parse["user"]["id"]


    # token_response = response_parse.get("auth")
    # token = token_response["access_token"]
    #
    # user_response = response.json().get("user")
    # user_name = user_response["name"]
    # user_email = user_response["email"]
    # user_pass = ts
    # id = user_response["id"]

    return token, user_name, user_email, user_pass, id
    # return cookie_value, user_name, user_email, user_pass
