import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDrop:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    index_and_questions = [
        ('0', "Сколько это стоит? И как оплатить?"),
        ('1', "Хочу сразу несколько самокатов! Так можно?"),
        ('2', "Как рассчитывается время аренды?"),
        ('3', "Можно ли заказать самокат прямо на сегодня?"),
        ('4', "Можно ли продлить заказ или вернуть самокат раньше?"),
        ('5', "Вы привозите зарядку вместе с самокатом?"),
        ('6', "Можно ли отменить заказ?"),
        ('7', "Я живу за МКАДом, привезёте?")
    ]

    @pytest.mark.parametrize("index, expected_question", index_and_questions)
    def test_faq_dropdown(self, index, expected_question):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        question_locator = (By.ID, f"accordion__heading-{index}")
        question_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(question_locator)
        )
        assert expected_question in question_element.text