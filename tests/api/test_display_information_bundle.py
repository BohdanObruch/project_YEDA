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
NAME_BUNDLE = os.getenv('name_bundle')


@tag("Displaying the bundle on the website")
def test_display_information_bundle():

    id_college = f'current_college_id={ID_COLLEGE}'

    response = yeda().get(
        f'/wl/colleges/{ID_COLLEGE}/bundle/{NAME_BUNDLE}', params=id_college
    )
    assert response.status_code == 200
    assert S(bundle) == response.json()
    assert response.json()["slug"] == NAME_BUNDLE
