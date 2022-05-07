from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.base import BasePageObject


class YandexModal(BasePageObject):
    LOCATOR_SELF = (By.CSS_SELECTOR, "div.popup2.modal.popup2_visible_yes")
    LOCATOR_CLOSE_BUTTON = (By.CSS_SELECTOR, "div.modal__close")

    def __init__(self, driver):
        super().__init__(driver, True)
        self.modal = self.try_find_element(self.driver, self.LOCATOR_SELF, 3)
        self.modal_present = bool(self.modal)
        if self.modal_present:
            self.close = self.modal.find_element(*self.LOCATOR_CLOSE_BUTTON)

    def is_modal_present(self):
        return self.modal_present

    def close_modal(self):
        self.close.click()
        WebDriverWait(self.modal, 3).until(EC.invisibility_of_element_located(self.LOCATOR_SELF))

