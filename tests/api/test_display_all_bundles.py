import requests
import os

from schemas.yeda import *
from pytest_voluptuous import S
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Display of all bundles on the college website")
def test_display_all_bundles():
    id_college = os.getenv('ID_COLLEGE')

    response = yeda().get(f'/wl/colleges/{id_college}/bundles')

    assert response.status_code == 200
    assert S(bundles) == response.json()

