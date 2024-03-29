import requests
import os
import json

from schemas.yeda import *
from pytest_voluptuous import S
from tests.conftest import *
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Filling out the student's account information")
def test_edit_profile_user(register_user):

    user_email = register_user[2]
    user_name = register_user[1]
    user_id = register_user[4]
    token_value = str("Bearer " + register_user[0])
    token = {"Authorization": token_value}

    registered_user = {
        "about": "Add a few lines about yourself",
        "city": "New York",
        "email": user_email,
        "name": user_name
    }

    response = yeda().put(
        '/wl/me',
        headers=token,
        data=registered_user
    )

    assert response.status_code == 200
    assert response.json()["user"]["email"] == user_email
    assert response.json()["user"]["username"] == user_name
    assert response.json()["user"]["id"] == user_id
