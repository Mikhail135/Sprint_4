import allure
import pytest
from data.faq_data import faq_data
from pages.home_page import HomePage
from locator.locator import Locator
from data import data

class TestFAQ:

    @allure.title("Проверка FAQ")
    @pytest.mark.parametrize("index, expected_question, expected_answer", faq_data)
    def test_faq_dropdown(self, index, expected_question, expected_answer, driver):
        home_page = HomePage(driver)
        home_page.get(data.site_link)
        question_locator = (Locator.question_locator[0], Locator.question_locator[1]+index)
        home_page.scroll_page(question_locator)
        question_element = home_page.find_element(question_locator)
        assert expected_question in question_element.text
        home_page.scroll_page_faq(question_element, index)
        answer_locator = (Locator.answer_locator[0], Locator.answer_locator[1]+index)
        answer_element = home_page.find_element(answer_locator)
        assert expected_answer in answer_element.text
