from selenium.webdriver.common.by import By
from PageObjects.base import BasePageObject


class YandexMediaViewer(BasePageObject):
    LOCATOR_SELF = (By.CSS_SELECTOR, ".MediaViewer")
    LOCATOR_BACK = (By.CSS_SELECTOR, ".CircleButton_type_prev")
    LOCATOR_NEXT = (By.CSS_SELECTOR, ".CircleButton_type_next")
    LOCATOR_IMG = (By.CSS_SELECTOR, ".MMImage-Origin")

    def __init__(self, driver, from_element=False):
        super().__init__(driver, from_element)
        self.back = self.init_element(self.LOCATOR_BACK)
        self.next = self.init_element(self.LOCATOR_NEXT)
        self.img = self.init_element(self.LOCATOR_IMG, False, True)

    def get_current_img_src(self):
        return self.img.get_attribute('src')

    def prev_img(self):
        self.back.click()

    def next_img(self):
        self.next.click()


