import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrderTop:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, comment",
        [
            ("Иван", "Иванов", "Москва", "Новогиреево", "89266664344", "01.01.2000", "Быстрее"),
            ("Петр", "Петров", "Санкт-Петербург", "Новокосино", "89876543210", "01.02.2002", "Я тороплюсь")
        ]
    )
    def test_order_flow(self, name, surname, address, metro, phone, date, comment):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        home_page = HomePage(self.driver)
        home_page.click_order_button_top()
        order_page = OrderPage(self.driver)
        order_page.fill_order_form(name, surname, address, metro, phone)
        order_page.submit_order()
        order_page.second_form_order(date, comment)
        assert 'Заказ оформлен' in order_page.order_text
