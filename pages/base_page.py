
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Подождать и найти элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание определенной страницы')
    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Возвращение текущего url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Клик на логотип Яндекс и открытие страницы в новом окне')
    def click_and_swith_to_new_window(self, locator):
        handles_before = self.driver.window_handles
        self.wait_and_find_element(locator).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(
            lambda driver: len(handles_before) != len(driver.window_handles))

        self.driver.switch_to.window(self.driver.window_handles[-1])
