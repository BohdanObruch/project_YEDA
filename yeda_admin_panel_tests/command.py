from selene.core.command import *
import selene
from selene.core.wait import Command
from selenium.webdriver import ActionChains


def drag_to(destination: selene.Element):
    def action(source: selene.Element):
        ActionChains(source.config.driver).drag_and_drop(source(), destination()).perform()

    return Command(f'drag to {destination}', action)