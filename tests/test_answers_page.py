import allure
import pytest

from conftest import driver
from pages.answers_page import Answers


class TestAnswers:

    @allure.title('Проверка: Вопросы о важном')
    @pytest.mark.parametrize('question, answer, true_answer',
                             [(Answers.question_1, Answers.answer_1, Answers.answer_text_1),
                              (Answers.question_2, Answers.answer_2, Answers.answer_text_2),
                              (Answers.question_3, Answers.answer_3, Answers.answer_text_3),
                              (Answers.question_4, Answers.answer_4, Answers.answer_text_4),
                              (Answers.question_5, Answers.answer_5, Answers.answer_text_5),
                              (Answers.question_6, Answers.answer_6, Answers.answer_text_6),
                              (Answers.question_7, Answers.answer_7, Answers.answer_text_7),
                              (Answers.question_8, Answers.answer_8, Answers.answer_text_8)])
    def test_question(self, driver, question, answer, true_answer):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question(question)
        text_answer = base_page.get_answer_text(answer)

        assert text_answer == true_answer




