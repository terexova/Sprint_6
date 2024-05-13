import allure

from conftest import driver
from pages.answers_page import Answers


class TestAnswers:

    @allure.title('Проверка: Вопросы о важном')
    @allure.description('Клик на вопрос и проверяем ответ')
    def test_question_1(self, driver):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question_1()
        answer = base_page.get_answer_1()

        assert answer.is_displayed()

    def test_question_2(self, driver):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question_2()
        answer = base_page.get_answer_2()

        assert answer.is_displayed()

    def test_question_3(self, driver):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question_3()
        answer = base_page.get_answer_3()

        assert answer.is_displayed()

    def test_question_4(self, driver):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question_4()
        answer = base_page.get_answer_4()

        assert answer.is_displayed()

    def test_question_5(self, driver):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question_5()
        answer = base_page.get_answer_5()

        assert answer.is_displayed()

    def test_question_6(self, driver):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question_6()
        answer = base_page.get_answer_6()

        assert answer.is_displayed()

    def test_question_7(self, driver):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question_7()
        answer = base_page.get_answer_7()

        assert answer.is_displayed()

    def test_question_8(self, driver):
        base_page = Answers(driver)
        base_page.open_page()
        base_page.click_cookie()
        base_page.click_question_8()
        answer = base_page.get_answer_8()

        assert answer.is_displayed()



