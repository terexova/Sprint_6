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

    @allure.step('Клик на вопрос')
    def click_question(self, locator):
        self.find_element(locator).click()

    @allure.step('Получение ответа')
    def get_answer_text(self, locator):
        return self.find_element(locator).text
