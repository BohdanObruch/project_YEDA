import requests
import os

from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Display of all courses on the college website")
def test_display_all_courses():
    id_college = os.getenv('ID_COLLEGE')

    current_college_id = f'current_college_id={id_college}'

    response = yeda().get(f'/wl/colleges/{id_college}/courses',
                          params=current_college_id,)

    assert response.status_code == 200
    assert S(courses) == response.json()
