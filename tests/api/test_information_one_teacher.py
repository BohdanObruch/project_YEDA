import requests
import os
import pytest

from schemas.yeda import *
from pytest_voluptuous import S
from yeda_admin_panel_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Displaying the lecturer and his information on the website")
def test_display_teacher_information():
    ID_TEACHER = os.getenv('id_teacher')
    ID_COLLEGE = os.getenv('id_college')

    params = f"username={ID_TEACHER}&current_college_id={ID_COLLEGE}"

    response = yeda().get(
        '/website/college/teacher',
        params=params
    )
    assert response.status_code == 200
    assert S(teacher) == response.json()
    assert response.json()["access_level"] == 3
    assert response.json()["id"] == int(ID_TEACHER)
