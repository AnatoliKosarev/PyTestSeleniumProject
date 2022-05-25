from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils.conf import TIMEOUT


def wait_until_element_is_visible(browser, locator, timeout=TIMEOUT):
    element = WebDriverWait(browser, timeout).until(ec.visibility_of_element_located(locator))
    return element


def wait_until_element_is_clickable(browser, locator, timeout=TIMEOUT):
    element = WebDriverWait(browser, timeout).until(ec.element_to_be_clickable(locator))
    return element


