import allure
from pages.base_page import BasePage
from locator.locator import Locator

class HomePage(BasePage):
    @allure.step("Клик по верней кнопке 'Заказть")
    def click_order_button_top(self):
        self.click(Locator.order_button_top)

    @allure.step("Клик по цетральной кнопке 'Заказть")
    def click_order_button_bottom(self):
        self.click(Locator.order_button_bottom)

    @allure.step("Проверка логотипа 'Самокат'")
    def is_scooter_logo_visible(self):
        return self.driver.find_element(*Locator.scooter_logo).is_displayed()

    @allure.step("Проверка логотипа 'Самокат'")
    def is_yandex_logo_visible(self):
        self.driver.find_element(*Locator.yandex_logo).click()
