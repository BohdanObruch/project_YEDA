import allure
import requests
import os
from allure_commons.types import AttachmentType
from selene.support.shared import browser
from dotenv import load_dotenv


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def get_url_video(session_id: str):
    api_browserstack = os.getenv('API_BROWSERSTACK')
    session = requests.Session()
    session.auth = (os.getenv('LOGIN'), os.getenv('KEY'))
    response = session.get(
        f'{api_browserstack}/sessions/{session_id}.json')
    return response.json().get('automation_session').get('video_url')


def add_video(session_id: str, name: str):
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + get_url_video(session_id) \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, name, AttachmentType.HTML, '.html')


def add_video_selenoid(browser):
    video_url = "http://92.118.149.155:8080/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
#
#


def screen_xml_dump(*, name=None):
    allure.attach(
        browser.driver.page_source,
        name=name or 'page xml dump',
        attachment_type=allure.attachment_type.XML,
    )


def screen_html_dump(*, name=None):
    allure.attach(
        browser.driver.page_source,
        name=name or 'page html dump',
        attachment_type=allure.attachment_type.HTML,
    )


def screenshot(*, name='screenshot'):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )
