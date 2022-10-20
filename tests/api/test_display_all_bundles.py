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


@tag("Display of all bundles on the college website")
def test_display_all_bundles():

    response = yeda().get(f'/wl/colleges/{ID_COLLEGE}/bundles')

    assert response.status_code == 200
    print(response.json())
    assert S(bundles) == response.json()

