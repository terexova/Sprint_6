
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_and_find_element_presence(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Возвращение текущего url')
    def get_current_url(self):
        return self.driver.current_url
