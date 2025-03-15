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

    index_and_answers = [
        ('0', "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        ('1', "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        ('2', "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды"
              " начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        ('3', "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        ('4', "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        ('5', "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься "
              "без передышек и во сне. Зарядка не понадобится."),
        ('6', "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        ('7', "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ]

    @pytest.mark.parametrize("index, expected_answer", index_and_answers)
    def test_faq_dropdown(self, index, expected_answer):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        question_locator = (By.ID, f"accordion__heading-{self.index_and_answers[-1][0]}")
        question_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(question_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)

        self.driver.find_element(By.ID, f"accordion__heading-{index}").click()
        answer_locator = (By.ID, f"accordion__panel-{index}")
        answer_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(answer_locator)
        )
        assert expected_answer in answer_element.text