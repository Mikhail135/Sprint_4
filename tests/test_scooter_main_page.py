import allure
from pages.home_page import HomePage
from locator.locator import Locator
from data import data


class TestLogoScooter:
    @allure.title("Проверка логотипа 'Самокат'")
    def test_yandex_change_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.get(data.site_link)
        home_page.is_scooter_logo_visible()
        home_page.find_element(Locator.scooter_logo)
        text_scooter = home_page.find_element(*Locator.order_button_top).text
        assert 'Заказать' in text_scooter
