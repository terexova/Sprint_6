
from data import UrlScooter
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Answers(BasePage):
    question_1 = [By.XPATH, "//div[@id='accordion__heading-0']"]
    answer_1 = [By.XPATH, "//div[@id='accordion__panel-0']"]

    question_2 = [By.XPATH, "//div[@id='accordion__heading-1']"]
    answer_2 = [By.XPATH, "//div[@id='accordion__panel-1']"]

    question_3 = [By.XPATH, "//div[@id='accordion__heading-2']"]
    answer_3 = [By.XPATH, "//div[@id='accordion__panel-2']"]

    question_4 = [By.XPATH, "//div[@id='accordion__heading-3']"]
    answer_4 = [By.XPATH, "//div[@id='accordion__panel-3']"]

    question_5 = [By.XPATH, "//div[@id='accordion__heading-4']"]
    answer_5 = [By.XPATH, "//div[@id='accordion__panel-4']"]

    question_6 = [By.XPATH, "//div[@id='accordion__heading-5']"]
    answer_6 = [By.XPATH, "//div[@id='accordion__panel-5']"]

    question_7 = [By.XPATH, "//div[@id='accordion__heading-6']"]
    answer_7 = [By.XPATH, "//div[@id='accordion__panel-6']"]

    question_8 = [By.XPATH, "//div[@id='accordion__heading-7']"]
    answer_8 = [By.XPATH, "//div[@id='accordion__panel-7']"]

    cookie = [By.XPATH, "//button[text() = 'да все привыкли']"]

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(UrlScooter.URL)

    def click_cookie(self):
        self.wait_and_find_element(self.cookie).click()

    def click_question_1(self):
        self.wait_and_find_element(self.question_1).click()

    def get_answer_1(self):
        return self.driver.find_element(*self.answer_1)


    def click_question_2(self):
        self.driver.find_element(*self.question_2).click()

    def get_answer_2(self):
        return self.driver.find_element(*self.answer_2)


    def click_question_3(self):
        self.driver.find_element(*self.question_3).click()

    def get_answer_3(self):
        return self.driver.find_element(*self.answer_3)


    def click_question_4(self):
        self.driver.find_element(*self.question_4).click()

    def get_answer_4(self):
        return self.driver.find_element(*self.answer_4)


    def click_question_5(self):
        self.driver.find_element(*self.question_5).click()

    def get_answer_5(self):
        return self.driver.find_element(*self.answer_5)


    def click_question_6(self):
        self.driver.find_element(*self.question_6).click()

    def get_answer_6(self):
        return self.driver.find_element(*self.answer_6)


    def click_question_7(self):
        self.driver.find_element(*self.question_7).click()

    def get_answer_7(self):
        return self.driver.find_element(*self.answer_7)


    def click_question_8(self):
        self.driver.find_element(*self.question_8).click()

    def get_answer_8(self):
        return self.driver.find_element(*self.answer_8)
