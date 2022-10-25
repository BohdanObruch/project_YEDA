import requests
import os

from schemas.yeda import *
from pytest_voluptuous import S
from yeda_admin_panel_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Display of all teachers on the college website")
def test_display_all_teachers():
    ID_COLLEGE = os.getenv('id_college')

    number_college = f'id={ID_COLLEGE}'

    response = yeda().get(
        '/website/college/teachers', params=number_college
    )
    assert response.status_code == 200
    assert S(teachers) == response.json()

