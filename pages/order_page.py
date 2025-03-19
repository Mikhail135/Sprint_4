import allure
from pages.base_page import BasePage
from locator.locator import Locator
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    @allure.step("Заполнение информации о клиенте")
    def fill_order_form(self, name, surname, address, metro, phone):
        self.send_keys(Locator.name_input, name)
        self.send_keys(Locator.surname_input, surname)
        self.send_keys(Locator.address_input, address)
        self.send_keys(Locator.metro_input, metro)
        metro_input = self.find_element(Locator.metro_input)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)
        self.send_keys(Locator.phone_input, phone)

    @allure.step("Нажатие кнопки 'Далее'")
    def submit_order(self):
        self.click(Locator.submit_button)

    @allure.step("Заполнение доп. информации по заказу")
    def second_form_order(self, date, comment):
        date_input = self.find_element(Locator.date_input)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        self.find_element(Locator.rental_dropdown)
        self.click(Locator.rental_dropdown)
        self.find_element(Locator.rental_period)
        self.click(Locator.rental_period)
        self.click(Locator.checkbox)
        self.send_keys(Locator.comment_input, comment)
        self.click(Locator.order_button)
        self.click(Locator.order_action_yes)


    @property
    def order_text(self):
        return self.get_text(Locator.order_completed)
