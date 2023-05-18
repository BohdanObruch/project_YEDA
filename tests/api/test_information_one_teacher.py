import requests
import os

from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title
from bs4 import BeautifulSoup
import json


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

    soup = BeautifulSoup(response.text, 'html.parser')
    json_data = json.loads(soup.text)

    assert response.status_code == 200
    assert S(teacher) == json_data
    assert json_data["access_level"] == 3
    assert json_data["id"] == int(id_teacher)
