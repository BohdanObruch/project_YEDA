import requests
import os
import pytest

from dotenv import load_dotenv
from schemas.yeda import *
from pytest_voluptuous import S
from yeda_admin_panel_tests.utils.sessions import yeda
from allure import tag


@pytest.fixture(autouse=True, scope='session')
def environment():
    load_dotenv()


ID_COLLEGE = os.getenv('id_college')


@tag("Displaying the course on the website")
def test_display_course():

    name_course = 'test-create-course-new-yeda'

    response = yeda().get(
        f'/wl/colleges/{ID_COLLEGE}/courses/' + name_course
    )
    assert response.status_code == 200
    assert S(course) == response.json()
    assert response.json()["slug_id"] == name_course
