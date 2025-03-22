import allure
from pages.home_page import HomePage
from locator.locator import Locator
from data import data

class TestLogoYandex:
    @allure.title("Проверка логотипа 'Яндекс'")
    def test_yandex_change_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.get(data.site_link)
        home_page.is_yandex_logo_visible()
        home_page.switch()
        dzen_text = home_page.find_element(Locator.dzen).text
        assert 'Главная' in dzen_text
