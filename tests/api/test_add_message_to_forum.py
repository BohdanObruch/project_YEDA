import requests
import lorem
import os

from schemas.yeda import *
from pytest_voluptuous import S
from tests.conftest import *
from diploma_project_tests.utils.sessions import yeda
from allure import tag, title


@tag('API')
@title("Add a message to the college course")
def test_add_message_to_forum(register_user):

    id_college = os.getenv('ID_COLLEGE')
    id_course = os.getenv('COURSE_ID')

    token_value = str("Bearer " + register_user[0])
    token = {"Authorization": token_value}

    id_user = register_user[4]
    user_name = register_user[1]

    current_college_id = f'current_college_id={id_college}'

    subject = lorem.sentence()
    text_message = lorem.paragraph()

    text_message = {
        "subject": subject,
        "text": text_message,
        "receive_notifications": False,
        "course_id": id_course
    }

    response = yeda().post('/wl/forum/threads',
                           headers=token,
                           params=current_college_id,
                           data=text_message
                           )

    assert response.status_code == 201
    assert S(message_forum) == response.json()
    assert response.json()["user"]["id"] == id_user
    assert response.json()["user"]["username"] == user_name
    assert response.json()["user"]["role"] == "student"
