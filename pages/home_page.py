from locator.locator import Locator
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_order_button_top(self):
        self.driver.find_element(*Locator.order_button_top).click()

    def click_order_button_bottom(self):
        self.driver.find_element(*Locator.order_button_bottom).click()

    def is_scooter_logo_visible(self):
        return self.driver.find_element(*Locator.scooter_logo).click()

    def is_yandex_logo_visible(self):
        return self.driver.find_element(*Locator.yandex_logo).click()
