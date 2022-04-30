from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator_type, locator):
        try:
            self.browser.find_element(locator_type, locator)
        except NoSuchElementException:
            return False

        return True
