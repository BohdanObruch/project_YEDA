import requests
import os
import pytest

from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Displaying the lecturer and his information on the website")
def test_display_teacher_information():
    id_teacher = os.getenv('ID_TEACHER')
    id_college = os.getenv('ID_COLLEGE')

    params = f"username={id_teacher}&current_college_id={id_college}"

    response = yeda().get(
        '/website/college/teacher',
        params=params
    )
    assert response.status_code == 200
    assert S(teacher) == response.json()
    assert response.json()["access_level"] == 3
    assert response.json()["id"] == int(id_teacher)
