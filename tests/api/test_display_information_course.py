import os
import requests

from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Displaying the course on the website")
def test_display_course():
    id_college = os.getenv('ID_COLLEGE')
    name_course_api = os.getenv('NAME_COURSE_API')

    response = yeda().get(
        f'/wl/colleges/{id_college}/courses/' + name_course_api
    )
    assert response.status_code == 200
    assert S(course) == response.json()
    assert response.json()["slug_id"] == name_course_api
