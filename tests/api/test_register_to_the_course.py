import requests
import os
import pytest

from schemas.yeda import *
from pytest_voluptuous import S
from tests.conftest import *
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Student registration for the course")
def test_register_to_the_course(register_user):
    college_id = os.getenv('ID_COLLEGE')
    course_id = os.getenv('COURSE_ID')

    token_value = str("Bearer " + register_user[0])
    token = {"Authorization": token_value}

    current_college_id = f'current_college_id={college_id}'

    id_user = register_user[4]

    response = yeda().post(
        f'/courses/{course_id}/enroll',
        headers=token,
        params=current_college_id
    )
    assert response.status_code == 201
    assert S(status_register_course) == response.json()
    assert response.json()["user_id"] == id_user
