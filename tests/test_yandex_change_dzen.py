import allure
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locator.locator import Locator


class TestLogoYandex:
    @allure.title("Проверка логотипа 'Яндекс'")
    def test_yandex_change_dzen(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        home_page = HomePage(driver)
        home_page.is_yandex_logo_visible()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[1])
        dzen_text = home_page.find_element(Locator.dzen).text
        assert 'Главная' in dzen_text
