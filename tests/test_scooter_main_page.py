from selenium import webdriver
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locator.locator import Locator


class TestLogoScooter:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_yandex_change_dzen(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        home_page = HomePage(self.driver)
        home_page.is_scooter_logo_visible()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(Locator.scooter_logo))
        text_scooter = self.driver.find_element(*Locator.order_button_top).text
        assert 'Заказать' in text_scooter
