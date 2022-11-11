# Diploma project on test automation in Python + Selene. 


* UI - https://yedalms.io/
* API - https://yedalms.io/
* Mobile - https://www.booking.com/

## The following functionality is covered
* UI (college admin panel tests)- https://yedalms.io/
    * ✅ Creating an article
    * ✅ Creating a bundle
    * ✅ Creating a course
    * ✅ Creating lessons
    * ✅ Creating a questionnaire(s) 
    * ✅ Creating a feedback form(survey)
    * ✅ Creating a student
    * ✅ Creating a lecturer
    * ✅ Filling the questionnaire with content
    * ✅ Filling the bundle with content

<br>
  
* API tests (college)- https://yedalms.io/
    * ✅ Adding a message to the forum
    * ✅ Signing in
    * ✅ Checking the display of all bundles
    * ✅ Checking the display of all courses
    * ✅ Checking the display of all college lecturers
    * ✅ Checking the display of bandle information
    * ✅ Checking the display of course information
    * ✅ Changing student information
    * ✅ Checking the display of lecturer information
    * ✅ Applying for course registration

<br>

* Android tests - https://www.booking.com/
    * ✅ Creating a list of favorites
    * ✅ Adding homes to favorites
    * ✅ Authorizing in the app
    * ✅ Deleting a place from your favorites
    * ✅ Registering a student 
    * ✅ Searching for attractions
    * ✅ Searching for housing reservations
    * ✅ Search for car rental
    * ✅ Search for cab reservations
    * ✅ Search for travel articles
  
<br>


## The project was implemented using

<p  align="left">
<code>
  <img src="resources/images/logo/python.svg" width="50" height="50"  alt="Python"/>
  <img src="resources/images/logo/selene.png" width="50" height="50"  alt="Selene"/>
  <img src="resources/images/logo/pytest.png" width="50" height="50"  alt="Pytest"/>
  <img src="resources/images/logo/pycharm.png" width="50" height="50"  alt="PyCharm"/>
  <img src="resources/images/logo/request.png" width="50" height="50"  alt="Requests"/>
  <img src="resources/images/logo/appium.svg" width="50" height="50"  alt="Appium"/>
  <img src="resources/images/logo/jenkins.png" width="50" height="50"  alt="Jenkins"/>
  <img src="resources/images/logo/selenoid.png" width="50" height="50"  alt="Selenoid"/>
  <img src="resources/images/logo/Allure.svg" width="50" height="50"  alt="Allure"/>
  <img src="resources/images/logo/GitHub.svg" width="50" height="50"  alt="Github"/>
  <img src="resources/images/logo/docker.svg" width="50" height="50"  alt="Docker"/>
  <img src="resources/images/logo/Allure_TO.svg" width="50" height="50"  alt="Allure TestOps"/>
  <img src="resources/images/logo/browserstack.svg" width="50" height="50"  alt="Browserstack"/>
  <img src="resources/images/logo/slack.svg" width="50" height="50"  alt="Slack"/>
  <img src="resources/images/logo/telegram.svg" width="50" height="50"  alt="Telegram"/>
  <img src="resources/images/logo/postman.png" width="50" height="50"  alt="Postman"/>
</code>
</p>

<br>

# <img width="6%" title="Jenkins" src="resources/images/logo/jenkins.png"> Autotests are run on the Jenkins server

<p align="center">
<img src="resources/images/jenkins_job.JPG" alt="Jenkins"/>
</p>
<br>

##  The build parameters in Jenkins:

* TESTS_FOLDER  (Selecting the folder to run the tests)
* BROWSER_VERSION (browser version, the default is 106.0)

<p align="center">
<img src="resources/images/jenkins_params.JPG" alt="Jenkins"/>
</p>
<br>

## Running tests

Local Launch:
```
pytest .
```

Remote launch:
```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest ${TESTS_FOLDER} --browser_version=${BROWSER_VERSION}
```
<br>

# <img width="4%" title="Allure" src="resources/images/logo/Allure.svg"> Allure
> Allure Framework is a flexible lightweight multi-language test report tool that not only shows a very concise representation of what have been tested in a neat web report form, but allows everyone participating in the development process to extract maximum of useful information from everyday execution of tests.

## Allure overview
> Different charts, metrics and statistic to easily analyze tests result
<p  align="left">
<code>
<img src="resources/images/allure_report.JPG" alt="Allure Report"/>
</code>
</p>

## Allure test result
> Here is a result of test executing.  
<p align="center">
<img src="resources/images/allure_report_more.JPG" alt="Allure Report"/>
</p>
<br>

## <img width="6%" title="Allure TestOps" src="resources/images/logo/Allure_TO.svg"> Allure Testops

## Dashboard 
> Dashboard with statuses of testcases on Allure Testops
<p align="center">
<img src="resources/images/allure_testops.JPG" alt="Allure Report"/>
</p>

## Test Cases
> Dashboard with statuses of test cases on Allure TestOps
<p align="center">
<img src="resources/images/allure_testops_test_cases.JPG" alt="Allure Report"/>
</p>
<br>


## Allure video result
> An example a short video how web tests executes on Selenoid server
<p  align="left">
<code>
<img width="100%" title="Allure video web test" src="resources/video/video_web.gif">
</code>
</p>
<br>

> An example a short video how mobile tests executes on Browserstack
<p  align="left">
<code>
<img width="100%" title="Allure video web test" src="resources/video/video_mobile.gif">
</code>
</p>

## <img width="6%" title="Browserstack" src="resources/images/logo/browserstack.svg"> Browserstack
> Mobile test log with results
<p  align="left">
<code>
<img width="100%" title="Browserstack" src="resources/images/browserstack.JPG">
</code>
</p>
<br>

# <img width="6%" title="Browserstack" src="resources/images/logo/telegram.svg"> Telegram notification
> Test results notifications to be sent to the specified telegram channel by the telegram bot
<p align="center">
<img src="resources/images/telegram.JPG" alt="Telegram"/>
</p>

# <img width="6%" title="Browserstack" src="resources/images/logo/slack.svg"> Slack notification
> Test results notifications to be sent to the specified Slack channel by the Slack bot
<p align="center">
<img src="resources/images/slack.JPG" alt="Slack"/>
</p>





