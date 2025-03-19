import allure
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locator.locator import Locator


class TestLogoScooter:
    @allure.title("Проверка логотипа 'Самокат'")
    def test_yandex_change_dzen(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        home_page = HomePage(driver)
        home_page.is_scooter_logo_visible()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locator.scooter_logo))
        text_scooter = driver.find_element(*Locator.order_button_top).text
        assert 'Заказать' in text_scooter
