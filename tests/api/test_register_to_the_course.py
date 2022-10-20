import requests
import os
import pytest

from dotenv import load_dotenv
from schemas.yeda import *
from pytest_voluptuous import S
from tests.conftest import *
from yeda_admin_panel_tests.utils.sessions import yeda
from allure import tag


@pytest.fixture(autouse=True, scope='session')
def environment():
    load_dotenv()


ID_COLLEGE = os.getenv('id_college')
ID_COURSE = os.getenv('course_id')


@tag("Student registration for the course")
def test_register_to_the_course(register_user):

    token_value = str("Bearer " + register_user[0])
    token = {"Authorization": token_value}

    current_college_id = f'current_college_id={ID_COLLEGE}'

    id_user = register_user[4]

    response = yeda().post(
        f'/courses/{ID_COURSE}/enroll',
        headers=token,
        params=current_college_id
    )
    assert response.status_code == 201
    assert S(status_register_course) == response.json()
    assert response.json()["user_id"] == id_user
