import os
import requests
from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title
from bs4 import BeautifulSoup
import json


@tag('API')
@title("Display of all teachers on the college website")
def test_display_all_teachers():
    id_college = os.getenv('ID_COLLEGE')

    params = {
        'id': id_college,
        'current_college_id': id_college
    }

    response = yeda().get(
        '/website/college/teachers', params=params
    )
    soup = BeautifulSoup(response.text, 'html.parser')
    json_data = json.loads(soup.text)

    assert response.status_code == 200
    assert S(teachers) == json_data
