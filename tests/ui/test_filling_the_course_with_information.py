import time

from selene import have, by
from selene.support.shared import browser

from yeda_admin_panel_tests.controls.utils import resource
from yeda_admin_panel_tests.pages.authorization_website import authorization_on_the_site
from yeda_admin_panel_tests import command


def test_filling_the_course(setup_browser):
    # browser = setup_browser

    authorization_on_the_site()

    browser.element('[href="/admin/courses"]').click()

    browser.element(
        '//*[text() = "CourseTemp50h (copy 1)"]').click()  # QA Automation course #f'//*[text() = "{name_course}"]

    browser.element('.page-header').should(have.text(' Editing Course'))
    """
    # Students
    browser.element('.panel [data-target="#students-collapse"] .fa-plus').click()
    browser.element('#import_users_file').send_keys(resource('template-courses.xlsx'))
    browser.element('.import-student:nth-child(1) .remove-from-import').click()
    browser.element('.jconfirm-buttons .btn-default:nth-child(1)').click()
    browser.element('.import-student:nth-child(3) .remove-from-import').click() #perform(command.js.scroll_into_view)
    browser.element('.jconfirm-buttons .btn-default:nth-child(1)').click()
    browser.element('.students-import #import-students').click()
    time.sleep(1)

    # Syllabus
    browser.element('.panel [data-target="#syllabus-collapse"] .fa-plus').click()
    browser.element('#checkbox-show-syllabus').click()

    # Create first syllabus
    browser.element('#btn-create-syllabus-item').click()
    browser.element('#item-title-syllabus').type('First line syllabus')
    browser.element('#createSyllabusSave').click()

     # Create second syllabus
    browser.element('#btn-create-syllabus-item').click()
    browser.element('#item-title-syllabus').type('Second line syllabus')
    browser.element('#createSyllabusSave').click()

     # Add information to the first syllabus
    browser.element('.syllabus_item:nth-child(1) .input-syllabus-item-file').send_keys(
        resource('CTFL-Syllabus-2018-GA.pdf'))
    browser.element('.syllabus_item:nth-child(1) .syllabus_item_open').click()
    
     # Add syllabus sub item #1
    browser.element('.syllabus_item:nth-child(1) .add-syllabus-subitem').click()
    browser.element('.syllabus_subitem .col').type('syllabus sub item #1')
    browser.element('.syllabus_subitem:nth-child(1) .input-syllabus-sub-item-file').send_keys(
        resource('Document_1.pdf'))
        
     # Add syllabus sub item #2
    browser.element('.syllabus_item:nth-child(1) .add-syllabus-subitem').click()
    browser.element('.syllabus_subitem:nth-child(2) .col').type('syllabus sub item #2')
    browser.element('.syllabus_subitem:nth-child(2) .input-syllabus-sub-item-file').send_keys(
        resource('Document_2.pdf'))
    browser.element('.syllabus_item:nth-child(1) .syllabus_item_save').click()

    # Add information to the second syllabus
    browser.element('.syllabus_item:nth-child(2) .input-syllabus-item-file').send_keys(resource('lesson_19.pdf'))
    browser.element('.syllabus_item:nth-child(2) .syllabus_item_open').click()
    
     # Add syllabus sub item #1
    browser.element('.syllabus_item:nth-child(2) .add-syllabus-subitem').click()
    browser.element('.syllabus_item:nth-child(2) .syllabus_subitem .col').type('syllabus sub item #3')
    browser.element('.syllabus_item:nth-child(2) .input-syllabus-sub-item-file').send_keys(resource('Document_3.pdf'))
     # Add syllabus sub item #2
    browser.element('.syllabus_item:nth-child(2) .add-syllabus-subitem').click()
    browser.element('.syllabus_item:nth-child(2) .syllabus_subitem:nth-child(2) .col').type('syllabus sub item #4')
    browser.element(
        '.syllabus_item:nth-child(2) .syllabus_subitem:nth-child(2) .input-syllabus-sub-item-file').send_keys(
        resource('Document_4.pdf'))
    browser.element('.syllabus_item:nth-child(2) .syllabus_item_save').click()

    time.sleep(2)

    browser.element('.syllabus_item:nth-child(1) .fa-minus').click()
    browser.element('.syllabus_item:nth-child(2) .fa-minus').click()

    # drag and drop syllabus

    first_syllabus = browser.element('.syllabus_item:nth-child(1)')
    second_syllabus = browser.element('.syllabus_item:nth-child(2)')

    second_syllabus.perform(command.drag_to(first_syllabus))
    #action.command(second_syllabus(), first_syllabus()).perform()

    # Quotes

    browser.element('.panel [data-target="#quotes-collapse"] .fa-plus').click()

    # First Quote
    browser.element('#createQuote').click()

    browser.element('#photo').send_keys(resource('Albert_Einstein.jpg'))
    time.sleep(2)
    browser.element('.quote-content').type('Before God we are all equally wise - and equally foolish.')
    browser.element('.quote-title').type('Albert Einstein')
    browser.element('.quote-form:nth-child(1) .on-air-radio').click()

    # add date
    browser.element('.date-wrapper .ui-datepicker-trigger').click()
    browser.element('.quote-form:nth-child(1) .hasDatepicker').perform(command.js.set_value('2022-08-19'))

    browser.element('.quote-form:nth-child(1) .quote_save').click()

    # Second Quote

    browser.element('#createQuote').click()

    browser.element('.quote-form:nth-child(2) #photo').send_keys(resource('albert-einstein2.jpg'))
    time.sleep(2)
    browser.element('.quote-form:nth-child(2) .quote-content').type('Imagination is more important than knowledge...')
    browser.element('.quote-form:nth-child(2) .quote-title').type('Albert Einstein')
    browser.element('.quote-form:nth-child(2) .not-on-air-radio').click()

    # add date
    browser.element('.date-wrapper .ui-datepicker-trigger').click()
    browser.element('.quote-form:nth-child(2) .hasDatepicker').perform(command.js.set_value('1954-01-03'))

    browser.element('.quote-form:nth-child(2) .quote_save').click()

    # drag and drop Quotes

    first_quotes = browser.element('#quotes-list .quote-form:nth-child(1)')
    second_quotes = browser.element('#quotes-list .quote-form:nth-child(2)')
    
    second_quotes.perform(command.drag_to(first_quotes))
    #action.command(second_quotes(), first_quotes()).perform()

    # Lecturers in the course
    browser.element('.panel [data-target="#l-collapse"] .fa-plus').click()

    # Add first lecturer
    browser.element('#find_lecturer').click().type(' אולגה מסקרפונה')
    browser.element('[data-id="48"]').click()
    browser.element('#add_lecturer').click()
    browser.element('.lecturer_name').with_(timeout=3).should(have.text('אולגה מסקרפונה'))

    # Add second lecturer
    browser.element('#find_lecturer').click().type(' יבגני אורין')
    browser.element('[data-id="190"]').click()
    browser.element('#add_lecturer').click()
    browser.element('[data-id="190"] .lecturer_name').with_(timeout=3).should(have.text('יבגני אורין'))
    """
    # Meetings Calendar
    browser.element('.panel [data-target="#meetings-calendar-collapse"] .fa-plus').perform(
        command.js.scroll_into_view).click()
    #
    # browser.element('#import-events-from-excel').perform(command.js.click)
    # browser.element('#import_events_file').send_keys(resource('schedule_example.xlsx'))  # schedule.xlsx
    # browser.element('#import-events-calendar-block .overheader').with_(timeout=5).should(have.text('Settings'))
    #
    # # Create Calendar with events
    # browser.element('#calendarImportName').type('Calendar with events')
    # browser.element('#calendarImportTitle').type('Events of the course')
    # browser.element('#calendarImportDescr').type('All course events are listed in this calendar')
    # browser.element('#calendarImportSave').click()
    # browser.element('.calendar-item .calendar_name').should(have.text('Events of the course'))
    #
    # # Create event
    # browser.element('.col .dropdown #dropdownMenuButton').click()
    # browser.element('#add-event-d-item').click()
    # browser.element('#createEventModalLabel').should(have.text('Add'))
    # browser.element('#createEventTitle').type('Final exam')
    # browser.element('#createEventExtraInfo').type('Checking Knowledge')
    # # browser.element('.modal-body .ui-datepicker-trigger').click()
    # browser.element('.modal-body .hasDatepicker').perform(command.js.set_value('2022-10-30'))
    # browser.element('#createEventBeginTimeHour').clear().type('10')
    # browser.element('#createEventBeginTimeMinute').clear().type('30')
    # browser.element('#createEventEndTimeHour').clear().type('21')
    # browser.element('#createEventEndTimeMinute').clear().type('10')
    # browser.element('#cerateEventCalendarSelect .dropdown-toggle').click()
    # browser.element('#cerateEventCalendarSelect .dropdown-menu').click()
    # browser.element('#createEventSave').click()
    #
    # # Create a Calendar
    # browser.element('.col .dropdown #dropdownMenuButton').click()
    # browser.element('#openCreateCalendarModal').click()
    # browser.element('#createCalendatModalLabel').should(have.text('Add +'))
    # browser.element('#createCalendarName').type('Calendar with course events')
    # browser.element('#createCalendarTitle').type('Checking knowledge of the course')
    # browser.element('#createCalendarIsPresented').click()
    # browser.element('#createCalendarDescr').type('All course events are listed in this calendar')
    # browser.element('#createCalendarSave').click()
    #
    # # Create Group
    # browser.element('.create-group').perform(command.js.scroll_into_view).click()
    # browser.element('.jconfirm-title').should(have.text('Write title for new calendars group'))
    # browser.element('.jconfirm-content .form-control').type('Grouping calendars with events by semester and subjects')
    # browser.element('.jconfirm-buttons .btn-blue').click() browser.element('.calendar-group-name')\
    # .should(have.text('Grouping calendars with events by semester and subjects'))

    # drag and drop calendars
    time.sleep(1)
    browser.element('//*[text()="Messages"]').perform(command.js.scroll_into_view).click()
    # time.sleep(1)
    first_calendar = browser.element('#default-group-calendars .calendar-item:nth-child(1) .btn')
    group_location = browser.element('#calendar-groups .group-calendars')

    first_calendar.perform(command.drag_to(group_location))


    # Create Sections
    browser.element('.panel [data-target="#s-collapse"] .fa-plus').click()
    browser.element('#checkbox-step-by-step').click()
    browser.element('#step-by-step-interval').clear().type('2')
    browser.element('#step-by-step-interval-save').click()

    # add first Section
    browser.element('#section-add-input').type('First module')
    browser.element('#section-add').click()

    # add second Section
    browser.element('#section-add-input').clear().type('Second module')
    browser.element('#section-add').click()

    # Adding learning content to the first module
    browser.element('.course-section:nth-child(1) .open-panel').click()
    browser.element('.course-section:nth-child(1) .section-is-required').click()

    # add lesson
    browser.element('.course-section:nth-child(1)  .add-course-section-item').click()
    browser.element('.course-section:nth-child(1) .course-section-item_input').type('מיקרו כלכלה - שיעור 2')
    browser.element('[data-id="414"]').click()

    # add questionnaire exam
    """
    Переписать ниже блок, так как баг с указанием имени урока/опросника
    """
    browser.element('#section-add-input').click()
    browser.element('.course-section:nth-child(1)  .add-course-section-item').perform(command.js.click)
    # browser.element('.course-section-item:nth-child(2) .course-section-item_input').click()
    browser.element('.course-section-item:nth-child(2) .course-section-item_type').element('[value="questionnaire"]') \
        .click()
    time.sleep(1)
    browser.element('.course-section-item:nth-child(2) .course-section-item_input').type('פרק כמותי 15 אלגברה')
    browser.element('[data-id="1284"]').with_(timeout=4).should(have.text('פרק כמותי 15 אלגברה')).click()
    browser.element('.course-section-item:nth-child(2) .questionnaire-item-duration').clear().type('60').press_enter()
    browser.element('.course-section-item:nth-child(2) .is-exam-required').click()
    browser.element('.course-section-item:nth-child(2) .questionnaire-item-passing-score').type('70').press_enter()

    # add questionnaire practice
    browser.element('.course-section:nth-child(1)  .add-course-section-item').perform(command.js.click)
    # browser.element('.course-section-item:nth-child(3) .course-section-item_input').click()
    browser.element('.course-section-item:nth-child(3) .course-section-item_type').click()
    browser.element('.course-section-item .course-section-item_type [value="questionnaire"]').click()
    browser.element('.course-section-item:nth-child(3) .course-section-item_input').type('פרק כמותי 10 אלגברה')
    browser.element('[data-id="1266"]').with_(timeout=4).should(have.text('פרק כמותי 10 אלגברה')).click()
    browser.element('.course-section-item:nth-child(3) .questionnaire-item-type').click().element('[value="2"]').click()
    browser.element('.course-section-item:nth-child(3) .is-exam-required').click()
    browser.element('.course-section-item:nth-child(3) .questionnaire-item-passing-score').type('80').press_enter()

    browser.element('.course-section:nth-child(1) .open-panel .fa-minus').click()

    # change second name section
    browser.element('.course-section:nth-child(2) .course-section_edit').click()
    browser.element('#courseSectionModal .modal-dialog').should(have.text('Edit Section Name'))
    browser.element('#courseSectionModal #section-title').clear().type('Second module part1')
    browser.element('#courseSectionModal #sectionModalSave').click()

    # Adding learning content to the second module
    browser.element('.course-section:nth-child(2) .open-panel').click()

    # add first survey
    browser.element('.course-section:nth-child(2)  .add-course-section-item').click()
    browser.element('.course-section:nth-child(2) .course-section-item_type').click().element(
        '[value="survey"]').click()
    browser.element('.course-section:nth-child(2) .course-section-item_input').type('שאלון לתלמיד במכללת איתן')
    browser.element('[data-id="95"]').with_(timeout=4).should(have.text('שאלון לתלמיד במכללת איתן')).click()

    # add second survey
    browser.element('.course-section:nth-child(2)  .add-course-section-item').click()
    browser.element('.course-section:nth-child(2) .course-section-item_type').element('[value="survey"]').click()
    browser.element('.course-section:nth-child(2) .course-section-item:nth-child(2) .course-section-item_input').type(
        'סקר הבנת הנושא ושביעות רצון')
    browser.element('[data-id="103"]').with_(timeout=4).should(have.text('סקר הבנת הנושא ושביעות רצון')).click()

    browser.element('.course-section:nth-child(2) .open-panel .fa-minus').click()

    # Smart community

    browser.element('.panel [data-target="#f-collapse"] .fa-plus').click()
    browser.element('#show_on_front_page').click()

    # Messages
    browser.element('.panel [data-target="#messages-collapse"] .fa-plus').click()
    browser.element('#messages-collapse [data-target="#send-message-form"]').click()
    browser.element('#messages-collapse .overheader-block .overheader:nth-child(2)').should(
        have.text('Post a message to users associated with the Course'))
    browser.element('#message_title').type('A message for all students in the course!')
    browser.element('#send-message-form .jodit-workplace .jodit-wysiwyg').type(
        'This message contains a list of additional literature that should be studied')
    browser.element('#message_files_input').send_keys(resource('template-courses.xlsx'))
    browser.element('[data-notify="message"]').with_(timeout=10).should(
        have.text('File has been successfully uploaded'))
    browser.element('#send-message-form  .btn-secondary.pl-5').click()
