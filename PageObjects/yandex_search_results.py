from selenium.webdriver.common.by import By
from PageObjects.base import BasePageObject


class YandexSearchResults(BasePageObject):
    LOCATOR_SELF = (By.CSS_SELECTOR, ".serp-list")
    LOCATOR_WAIT_FOR = (By.CSS_SELECTOR, ".serp-list .serp-item")
    LOCATOR_ITEMS = (By.CSS_SELECTOR, ".serp-item")

    def __init__(self, driver, from_element=False):
        super().__init__(driver, from_element)

        self.results = self.init_element(self.LOCATOR_ITEMS, True)

    def get_items(self):
        return self.results.get_value()
