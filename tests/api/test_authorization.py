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


@tag("User authorization on the website")
def test_authorization_user(register_user):

    user_name = register_user[1]
    user_email = register_user[2]
    user_password = register_user[3]

    registered_user = {
        "username": f"{user_name}",
        "password": f"{user_password}",
        "fieldname": "username",
        "college_id": ID_COLLEGE
    }
    response = yeda().post('/auth/login',
                           data=registered_user
                           )

    assert response.status_code == 200
    assert S(user) == response.json()
    assert response.json()["user"]["username"] == user_name
    assert response.json()["user"]["email"] == user_email
