import json
import logging
import calendar
import time
import datetime as DT
import os

import curlify as curlify
from requests import Session
import allure
from dotenv import load_dotenv


def allure_request_logger(function):
    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        message = curlify.to_curl(response.request)
        logging.info(f'{response.status_code} {message}')
        allure.attach(
            body=message.encode('utf8'),
            name=f'Request {response.request.method} {response.status_code}',
            attachment_type=allure.attachment_type.TEXT,
            extension='txt'
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4, ensure_ascii=False).encode('utf8'),
                name=f'Response {response.request.method}',
                attachment_type=allure.attachment_type.JSON,
                extension='json'
            )
        except ValueError as error:
            allure.attach(
                body=response.text.encode('utf8'),
                name=f'NOT Json Response {response.request.method}',
                attachment_type=allure.attachment_type.JSON,
                extension='json'
            )
        return response

    return wrapper


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    @allure_request_logger
    def request(self, method, url, **kwargs):
        with allure.step(f'{method} {url}'):
            response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
        return response


class UserApi:
    def create_user(self):
        id_college = os.environ.get('ID_COLLEGE')

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
            "college_id": id_college,
            "signed": f"{now_time}"
        }

        return user


user_api = UserApi()
