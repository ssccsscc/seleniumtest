from selenium.webdriver.common.by import By
from PageObjects.base import BasePageObject


class YandexSearchResult(BasePageObject):
    LOCATOR_SELF = (By.CSS_SELECTOR, ".serp-item")
    LOCATOR_LINK = (By.CSS_SELECTOR, "a")

    def __init__(self, driver, from_element=False):
        super().__init__(driver, from_element)
        self.link = self.init_element(self.LOCATOR_LINK)

    def get_link(self):
        return str(self.link.get_attribute('href'))

    def click_link(self):
        self.link.click()
