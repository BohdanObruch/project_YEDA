import calendar
import time


class Bundles:

    duration = '12 months'
    prerequisites = 'no limits'
    video_link = 'https://vimeo.com/437087249'
    short_description = 'This bundle about how to learn QA'
    description_line1 = 'QA Automation'
    description_line2 = 'This course about how to learn QA'
    picture = 'circle.png'
    video = 'QA.mp4'
    seo_title = 'QA Bundle Automation'
    seo_description = 'This bundle about how to learn Automation'
    start_date = '2023-02-01'
    end_date = '2023-02-26'
    normal_price = 150
    discount_price = 80
    file_with_users = 'template-courses.xlsx'
    name_first_course = 'קורס מאקרו כלכלה'
    full_name_first_course = 'קורס מאקרו כלכלה קורס מאקרו כלכלה'
    date_closed_first_course = '2022-11-15'
    name_second_course = 'קורס מאקרו כלכלה'
    full_name_second_course = 'קורס מאקרו כלכלה'
    date_closed_second_course = '2022-12-10'


class Lessons:
    normal_price = 100
    discount_price = 75
    title_lesson = 'Microeconomics - lesson 1'
    description_text = 'The return curve - first part. The structure of the curve based on the factors of production. ' \
                       'Allocation of factors of production according to the principle of comparative advantage. '
    document = 'Document_1.pdf'
    table = 'schedule.xlsx'
    name_lecturer = 'אולגה מסקרפונה'
    title_first_part_lesson = 'Microeconomics Lesson 1 - Part A'
    video_first_part_lesson = 'Mathematics.mp4'
    text_message = 'Video was uploaded and is being transcoded by vimeo.\n' \
                   'This may take some time.\n' \
                   'You can save now and check for image later.'
    title_second_part_lesson = 'Microeconomics Lesson 1 - Part B'
    video_second_part_lesson = 'Mathematics2.mp4'
    name_lesson = 'Microeconomics - lesson 1'


class Users:
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)
    name_user = ('Anna' + str(ts))
    email = (name_user + '@gmail.com')
    phone_number = ts
    city = 'Krakow'
    password = ts


class Teacher:
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)
    name_teacher = ('Pavel' + str(ts))
    email = (name_teacher + '@gmail.com')
    phone_number = ts
    picture = 'Albert_Einstein.jpg'
    seo_title = 'SEO Title'
    seo_description = 'SEO Description'
    positions_teacher = 'Professor of the highest category'
    short_description = 'Lecturer for the economy'
    description = 'Expert in everything related to security, political, family and black economy'


class Questionnaire:
    short_description = 'Here is a matriculation in English model E. This matriculation is for practice only, ' \
                        'so you can take your time and solve it slowly and thoroughly. Successfully! '
    description = 'The above exercises are designed to reset/find theoretical gaps in your study process.'
    picture = 'mathematics.jpg'
    count_questions = 3
    size_picture = 400
    first_title_chapters = 'mathematics'
    first_multiplier = 1
    first_categories = 'correct answer'
    subcategories = 'higher mathematics'
    first_resource = 'questionnaire1.jpeg'
    second_resource = 'questionnaire2.jpeg'
    name_first_tag = 'mathematics'
    third_resource = 'Mathematics.mp4'
    text_video_transcoding = 'Video was uploaded and is being transcoded by vimeo.\n' \
                             'This may take some time.\nYou can save now and check for image later.'
    answer_first = 1
    answer_second = 2
    answer_third = 3
    answer_fourth = 4
    second_title_chapters = 'English'
    second_multiplier = 2
    second_categories = 'Reading passages'
    fourth_resource = 'english.png'
    name_second_tag = 'English'
    first_answer = 'The method used for testing science students.'
    second_answer = 'The kinds of games that are used in science classes.'
    third_answer = 'The way that sciences are taught in high school.'
    fourth_answer = 'The subjects taught in science classes.'
    third_question = 'Planets closest to the Sun (called terrestrial planets)'
    name_third_tag = 'Solar System'
    first_answer_third_question = 'Mercury'
    second_answer_third_question = 'Jupiter'
    third_answer_third_question = 'Venus'
    fourth_answer_third_question = 'Uranus'
    fifth_answer_third_question = 'Earth'
    sixth_answer_third_question = 'Neptune'
    seventh_answer_third_question = 'Mars'
    eighth_answer_third_question = 'Saturn'
    first_questionnaire_title = 'Questionnaire Chapter #1'
    second_questionnaire_title = 'Questionnaire Chapter #2'
    third_questionnaire_title = 'Questionnaire Chapter #3'


class Course:
    short_description = 'This course about how to learn QA Automation'
    description = 'This course about how to learn QA Automation and Manual'
    duration = '12 month'
    prerequisites = 'Not have'
    picture = 'circle.png'
    description_line1 = 'QA Automation'
    description_line2 = 'This course about how to learn QA'
    table = 'template-courses.xlsx'
    file = 'lesson_19.pdf'
    seo_title = 'QA Automation'
    seo_description = 'This course about how to learn QA Automation'
    seo_author = 'QA'
    start_date = '2023-01-01'
    end_date = '2023-02-28'
    normal_price = 100
    discount_price = 60
