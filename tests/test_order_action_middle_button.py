import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data.data import order_data
from locator.locator import Locator
from data import data



class TestOrderMiddle:

    @allure.title("Проверка создания заказа через центральную кнопку 'Заказать'")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, comment",
        order_data
    )
    def test_order_flow(self, driver, name, surname, address, metro, phone, date, comment):
        home_page = HomePage(driver)
        home_page.get(data.site_link)
        home_page.scroll_page(Locator.order_button_bottom)
        home_page.click_order_button_bottom()
        order_page = OrderPage(driver)
        order_page.fill_order_form(name, surname, address, metro, phone)
        order_page.submit_order()
        order_page.second_form_order(date, comment)

        assert 'Заказ оформлен' in order_page.order_text

