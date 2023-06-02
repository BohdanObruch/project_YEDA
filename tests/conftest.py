import os
import pytest

from datetime import date
from appium import webdriver
from selene.support.shared import browser
from dotenv import dotenv_values, load_dotenv
from diploma_project_tests.controls import attach


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


dotenv = dotenv_values()


@pytest.fixture(scope='function')
def setup():
    linkApp = os.getenv('LINK_APP')

    desired_capabilities = ({
        "platformName": "android",
        "platformVersion": "11.0",
        "deviceName": "Samsung Galaxy S21",
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

    print(userName, accessKey, remoteUrl)
    browser.config.driver = webdriver.Remote(f"http://{userName}:{accessKey}@{remoteUrl}/wd/hub", desired_capabilities)
    browser.config.timeout = 4
    session_id = browser.config.driver.session_id

    yield

    attach.add_video(session_id, 'Test video')
    attach.screenshot(name='Last screenshot')
    attach.screen_xml_dump()

    browser.quit()
