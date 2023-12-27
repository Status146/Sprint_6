from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from conftest import driver
from data import AnswersText
import pytest
import allure


class TestQuestionsMainPage:
    @allure.title('Проверка ответов на вопросы из выпадающего списка «Вопросы о важном»')
    @pytest.mark.parametrize('number, expected_answer', AnswersText.answers)
    def test_question(self, driver, number, expected_answer):
        main_page = MainPage(driver)
        main_page.get_cookies(MainPageLocators.COOKIES_BUTTON)
        main_page.scroll(MainPageLocators.LAST_QUESTION)
        main_page.click_question(number)
        answer = main_page.get_answer(number)
        assert answer == expected_answer
        