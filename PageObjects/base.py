from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Element:
    def __init__(self, parent, locator, dynamic=False, multiple=False):
        self.locator = locator
        self.dynamic = dynamic
        self.multiple = multiple
        self.parent = parent
        self._element = False

        if not self.dynamic:
            self._find_element()

    def _find_element(self):
        if self.multiple:
            self._element = BasePageObject.find_elements(self.parent, self.locator)
        else:
            self._element = BasePageObject.find_element(self.parent, self.locator)

    def get_value(self):
        if self.dynamic:
            self._find_element()
        return self._element

    def __getattr__(self, name):
        return self.get_value().__getattribute__(name)

    def __iter__(self):
        return self.get_value().__iter__()

    def __getitem__(self, item):
        return self.get_value().__getitem__(item)


class BasePageObject:
    TIMEOUT = 3
    LOCATOR_SELF = False
    LOCATOR_WAIT_FOR = False

    def __init__(self, driver, from_element=False):
        self.driver = driver
        self.current_url = self.driver.current_url
        self.handles = self.driver.window_handles
        if self.LOCATOR_WAIT_FOR:
            self.wait_for_element(self.LOCATOR_WAIT_FOR)
        self.element = from_element
        if not from_element:
            self.element = self.find_element(self.driver, self.LOCATOR_SELF)

    def try_find_element(self, where, locator, time=TIMEOUT):
        try:
            return self.find_element(where, locator, time)
        except TimeoutException:
            return False

    def init_element(self, locator, multiple=False, dynamic=False, parent=False):
        if not parent:
            parent = self.element
        return Element(parent, locator, dynamic, multiple)

    @staticmethod
    def find_element(where, locator, time=TIMEOUT):
        return WebDriverWait(where, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Невозможно найти элемент {locator}")

    @staticmethod
    def find_elements(where, locator, time=TIMEOUT):
        return WebDriverWait(where, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Невозможно найти элемент {locator}")

    def wait_for_element(self, locator, time=TIMEOUT):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_till_page_changed(self, time=TIMEOUT):
        WebDriverWait(self.driver, time).until(EC.url_changes(self.current_url))
        self.current_url = self.driver.current_url

    def wait_till_window_opened(self, time=TIMEOUT):
        WebDriverWait(self.driver, time).until(EC.new_window_is_opened(self.handles))
        self.handles = self.driver.window_handles

    def switch_to_window(self, num):
        self.driver.switch_to.window(self.driver.window_handles[num])

