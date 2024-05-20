import allure

from data import UrlScooter
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Answers(BasePage):
    question_1 = [By.XPATH, "//div[@id='accordion__heading-0']"]
    answer_1 = [By.XPATH, "//div[@id='accordion__panel-0']"]
    answer_text_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    question_2 = [By.XPATH, "//div[@id='accordion__heading-1']"]
    answer_2 = [By.XPATH, "//div[@id='accordion__panel-1']"]
    answer_text_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    question_3 = [By.XPATH, "//div[@id='accordion__heading-2']"]
    answer_3 = [By.XPATH, "//div[@id='accordion__panel-2']"]
    answer_text_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    question_4 = [By.XPATH, "//div[@id='accordion__heading-3']"]
    answer_4 = [By.XPATH, "//div[@id='accordion__panel-3']"]
    answer_text_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    question_5 = [By.XPATH, "//div[@id='accordion__heading-4']"]
    answer_5 = [By.XPATH, "//div[@id='accordion__panel-4']"]
    answer_text_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    question_6 = [By.XPATH, "//div[@id='accordion__heading-5']"]
    answer_6 = [By.XPATH, "//div[@id='accordion__panel-5']"]
    answer_text_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    question_7 = [By.XPATH, "//div[@id='accordion__heading-6']"]
    answer_7 = [By.XPATH, "//div[@id='accordion__panel-6']"]
    answer_text_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    question_8 = [By.XPATH, "//div[@id='accordion__heading-7']"]
    answer_8 = [By.XPATH, "//div[@id='accordion__panel-7']"]
    answer_text_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    cookie = [By.XPATH, "//button[text() = 'да все привыкли']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы Яндекс.Самокат')
    def open_page(self):
        self.open_url(UrlScooter.URL)

    @allure.step('Клик на принятие Cookie')
    def click_cookie(self):
        self.wait_and_find_element(self.cookie).click()

    @allure.step('Клик на вопрос 1 "Сколько это стоит? И как оплатить?"')
    def click_question_1(self):
        self.wait_and_find_element(self.question_1).click()

    @allure.step('Ответ на вопрос 1')
    def get_answer_1(self):
        return self.driver.find_element(*self.answer_1)

    @allure.step('Клик на вопрос 2 "Хочу сразу несколько самокатов! Так можно?"')
    def click_question_2(self):
        self.driver.find_element(*self.question_2).click()

    @allure.step('Ответ на вопрос 2')
    def get_answer_2(self):
        return self.driver.find_element(*self.answer_2)

    @allure.step('Клик на вопрос 3 "Как рассчитывается время аренды?"')
    def click_question_3(self):
        self.driver.find_element(*self.question_3).click()

    @allure.step('Ответ на вопрос 3')
    def get_answer_3(self):
        return self.driver.find_element(*self.answer_3)

    @allure.step('Клик на вопрос 4 "Можно ли заказать самокат прямо на сегодня?"')
    def click_question_4(self):
        self.driver.find_element(*self.question_4).click()

    @allure.step('Ответ на вопрос 4')
    def get_answer_4(self):
        return self.driver.find_element(*self.answer_4)

    @allure.step('Клик на вопрос 5 "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_question_5(self):
        self.driver.find_element(*self.question_5).click()

    @allure.step('Ответ на вопрос 5')
    def get_answer_5(self):
        return self.driver.find_element(*self.answer_5)

    @allure.step('Клик на вопрос 6 "Вы привозите зарядку вместе с самокатом?"')
    def click_question_6(self):
        self.driver.find_element(*self.question_6).click()

    @allure.step('Ответ на вопрос 6')
    def get_answer_6(self):
        return self.driver.find_element(*self.answer_6)

    @allure.step('Клик на вопрос 7 "Можно ли отменить заказ?"')
    def click_question_7(self):
        self.driver.find_element(*self.question_7).click()

    @allure.step('Ответ на вопрос 7')
    def get_answer_7(self):
        return self.driver.find_element(*self.answer_7)

    @allure.step('Клик на вопрос 8 "Я жизу за МКАДом, привезёте?"')
    def click_question_8(self):
        self.driver.find_element(*self.question_8).click()

    @allure.step('Ответ на вопрос 8')
    def get_answer_8(self):
        return self.driver.find_element(*self.answer_8)

    @allure.step('Клик на вопрос')
    def click_question(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получение ответа')
    def get_answer_text(self, locator):
        return self.driver.find_element(*locator).text
