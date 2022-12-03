from selene.core.command import *
import selene
from selene.core.wait import Command
from selenium.webdriver import ActionChains
from selene.support.shared import browser


def drag_to(destination: selene.Element):
    def action(source: selene.Element):
        ActionChains(source.config.driver).drag_and_drop(source(), destination()).perform()

    return Command(f'drag to {destination}', action)


class SwipeHelper:

    def swipe_to_close_wallet_message(self):
        browser.driver.swipe(720, 683, 720, 2070, 400)
        return self

    def swipe_to_down(self):
        browser.driver.swipe(470, 1400, 470, -900, 330)
        return self

    def swipe_to_right(self):
        browser.driver.swipe(913, 319, 141, 319, 400)#975
        return self

    def swipe_to_down_one_block(self):
        browser.driver.swipe(470, 1400, 470, 600, 330)
        return self


swipe_helper = SwipeHelper()
