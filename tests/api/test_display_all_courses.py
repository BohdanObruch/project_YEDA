import requests
import os

from schemas.yeda import *
from pytest_voluptuous import S
from yeda_admin_panel_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Display of all courses on the college website")
def test_display_all_courses():
    ID_COLLEGE = os.getenv('id_college')

    response = yeda().get(f'/wl/colleges/{ID_COLLEGE}/courses')

    assert response.status_code == 200
    # print(response.json())
    assert S(courses) == response.json()
