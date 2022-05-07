from selenium.webdriver.common.by import By
from PageObjects.base import BasePageObject


class YandexImagesPopularRequests(BasePageObject):
    LOCATOR_SELF = (By.CSS_SELECTOR, ".PopularRequestList")
    LOCATOR_ITEM_LINK = (By.CSS_SELECTOR, ".PopularRequestList-Item a")
    LOCATOR_ITEM_LINK_TEXT = (By.CSS_SELECTOR, ".PopularRequestList-SearchText")

    def __init__(self, driver, from_element=False):
        super().__init__(driver, from_element)
        self.items = self.init_element(self.LOCATOR_ITEM_LINK, True)
        self.links = {}
        for item in self.items:
            item_name = item.find_element(*self.LOCATOR_ITEM_LINK_TEXT)
            self.links[item_name.text] = item

    def get_link_names(self):
        return list(self.links.keys())

    def click_on_link_by_name(self, link_name):
        self.links[link_name].click()


