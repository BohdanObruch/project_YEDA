from selene.core import command
from selene.core.entity import Element
from selene.support.shared import browser


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def set_by_click(self, data_day='12', data_month='4', data_year='1954'):
        self.element.click()

        browser.element(f'[data-year="{data_year}"]').click()
        browser.element(f'[data-month="{data_month}"]').click()
        browser.element(f'.ui-state-default{data_day}').click()

