import os
import requests

from schemas.yeda import *
from pytest_voluptuous import S
from yeda_admin_panel_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Displaying the course on the website")
def test_display_course():
    ID_COLLEGE = os.getenv('id_college')
    NAME_COURSE = os.getenv('name_course_api')

    response = yeda().get(
        f'/wl/colleges/{ID_COLLEGE}/courses/' + NAME_COURSE
    )
    assert response.status_code == 200
    assert S(course) == response.json()
    assert response.json()["slug_id"] == NAME_COURSE
