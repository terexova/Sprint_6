import allure
from selenium.webdriver.support.wait import WebDriverWait

from data import UrlScooter
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    BUTTON_REGISTRATION_UP = (By.XPATH, "//button[text() = 'Заказать']")
    LOGIN_NAME = (By.XPATH, "//[placeholder() = '* Имя']/following-sibling::input")
    LOGIN_LAST_NAME = (By.XPATH, "//[placeholder() = '* Фамилия']/following-sibling::input")
    LOGIN_ADDRESS = (By.XPATH, "//[placeholder() = '* Адрес: куда привезти заказ']/following-sibling::input")
    METRO_STATION = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    STATION = (By.CSS_SELECTOR, 'div.Order_Text__2broi')

    COOKIE = [By.XPATH, "//button[text() = 'да все привыкли']"]
    BUTTON_REGISTRATION_DOWN = (By.XPATH, './/button[contains(@class,"Button_Middle__1CSJM")][text()="Заказать"]')
    LOGO_SCOOTER = (By.CSS_SELECTOR, 'a.Header_LogoScooter__3lsAR')
    LOGO_YANDEX = (By.CSS_SELECTOR, 'a.Header_LogoYandex__3TSOI')
    DZEN = (By.XPATH, "//span[@tabindex='0']")


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы Яндекс.Самокат')
    def open_page(self):
        self.open_url(UrlScooter.URL)

    @allure.step('Клик на принятие Cookie')
    def click_cookie(self):
        self.wait_and_find_element(self.COOKIE).click()

    @allure.step('Клик на кнопку Заказать вверху страницы')
    def click_order_up(self):
        self.wait_and_find_element(self.BUTTON_REGISTRATION_UP).click()

    @allure.step('Прокрутка страницы вниз')
    def scroll_page(self):
        button = self.wait_and_find_element_presence(self.BUTTON_REGISTRATION_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)

    @allure.step('Клик на кнопку Заказать внизу страницы')
    def click_order_down(self):
        self.driver.find_element(*self.BUTTON_REGISTRATION_DOWN).click()

    @allure.step('Клик на логотип Самоката')
    def click_logo_Scooter(self):
        self.wait_and_find_element(self.LOGO_SCOOTER).click()

    @allure.step('Клик на логотип Яндекс')
    def click_logo_Yandex_and_go(self):
        handles_before = self.driver.window_handles
        self.wait_and_find_element(self.LOGO_YANDEX).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(
            lambda driver: len(handles_before) != len(driver.window_handles))

        self.driver.switch_to.window(self.driver.window_handles[-1])












