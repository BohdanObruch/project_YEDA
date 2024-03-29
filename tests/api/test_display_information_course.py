import os
import requests

from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Displaying the course on the website")
def test_display_course(register_user):
    id_college = os.getenv('ID_COLLEGE')
    name_course_api = os.getenv('NAME_COURSE_API')

    token_value = str("Bearer " + register_user[0])
    token = {"Authorization": token_value}

    current_college_id = f'current_college_id={id_college}'

    response = yeda().get(
        f'/wl/colleges/{id_college}/courses/' + name_course_api,
        headers=token,
        params=current_college_id)

    assert response.status_code == 200
    assert S(course) == response.json()
    assert response.json()["slug_id"] == name_course_api
