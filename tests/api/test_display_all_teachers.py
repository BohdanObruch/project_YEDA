import requests
import os

from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Display of all teachers on the college website")
def test_display_all_teachers():
    id_college = os.getenv('ID_COLLEGE')

    number_college = f'id={id_college}'

    response = yeda().get(
        '/website/college/teachers', params=number_college
    )
    assert response.status_code == 200
    assert S(teachers) == response.json()

