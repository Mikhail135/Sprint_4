import allure
from pages.base_page import BasePage
from locator.locator import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    @allure.step("Прокрутка страницы для faq")
    def scroll_page_faq(self, question_element, index):
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)
        self.driver.find_element(Locator.question_locator[0], Locator.question_locator[1]+index).click()

    @allure.step("Прокрутка страницы")
    def scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переход на сайт")
    def get(self, link):
        self.driver.get(link)

    @allure.step("Переход по вкладкам")
    def switch(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

