from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageObjects.base import BasePageObject


class YandexSearchForm(BasePageObject):
    LOCATOR_SELF = (By.CSS_SELECTOR, "form.search2")
    LOCATOR_INPUT = (By.XPATH, ".//input[@name='text']")
    LOCATOR_SUGGESTIONS = (By.CSS_SELECTOR, "ul.mini-suggest__popup-content")
    LOCATOR_SUGGESTIONS_ITEMS = (By.CSS_SELECTOR, "li.mini-suggest__item")

    def __init__(self, driver, from_element=False):
        super().__init__(driver, from_element)
        self.input = self.init_element(self.LOCATOR_INPUT)
        self.suggestion = self.init_element(self.LOCATOR_SUGGESTIONS, False, False, self.driver)
        self.suggestion_items = self.init_element(self.LOCATOR_SUGGESTIONS_ITEMS, True, True, self.suggestion)

    def input_into_search(self, text):
        self.input.click()
        self.input.send_keys(text)

    def get_suggestions_texts(self):
        return list(map(lambda item: item.text, self.suggestion_items))

    def search_using_enter(self):
        self.input.send_keys(Keys.RETURN)

    def get_search_text(self):
        return self.input.get_property("value")
