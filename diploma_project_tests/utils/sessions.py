import os
from diploma_project_tests.utils.requests_helper import BaseSession


def yeda() -> BaseSession:
    api_url = os.environ.get('API_URL')
    return BaseSession(base_url=api_url)


