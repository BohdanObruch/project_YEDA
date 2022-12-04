import requests
import os

from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Displaying the bundle on the website")
def test_display_information_bundle():
    college_id = os.getenv('ID_COLLEGE')
    name_bundle = os.getenv('NAME_BUNDLE')

    id_college = f'current_college_id={college_id}'

    response = yeda().get(
        f'/wl/colleges/{college_id}/bundle/{name_bundle}', params=id_college
    )
    assert response.status_code == 200
    assert S(bundle) == response.json()
    assert response.json()["slug"] == name_bundle
