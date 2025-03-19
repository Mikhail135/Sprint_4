import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.faq_data import faq_data

class TestFAQ:

    @allure.title("Проверка FAQ")
    @pytest.mark.parametrize("index, expected_question, expected_answer", faq_data)
    def test_faq_dropdown(self, index, expected_question, expected_answer, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_locator = (By.ID, f"accordion__heading-{index}")
        question_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(question_locator)
        )

        assert expected_question in question_element.text

        driver.execute_script("arguments[0].scrollIntoView();", question_element)
        driver.find_element(By.ID, f"accordion__heading-{index}").click()

        answer_locator = (By.ID, f"accordion__panel-{index}")
        answer_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(answer_locator)
        )
        assert expected_answer in answer_element.text
