import os
from diploma_project_tests.utils.requests_helper import BaseSession
from dotenv import load_dotenv


def yeda() -> BaseSession:
    yeda_url = os.getenv('api_url_yeda')
    return BaseSession(base_url=yeda_url)


