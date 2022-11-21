from allure import title, tag
from diploma_project_tests.model.accept_cookie import *
from diploma_project_tests.model.authorization_booking import *
from diploma_project_tests.model.verify_booking import *


@tag('Browserstack mobile')
@title('Authorization')
def test_authorization(setup):
    accept_cookie_settings()
    authorization()
    # verify_showing_welcome_message()
    verify_search_capability()



