import allure

from data import UrlScooter
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    LOGIN_NAME = (By.XPATH, "//input[@placeholder = '* Имя']")
    LOGIN_LAST_NAME = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    LOGIN_ADDRESS = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    STATION = (By.CSS_SELECTOR, 'div.Order_Text__2broi')
    PHONE = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text() = 'Далее']")
    DELIVERY = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    DELIVERY_DAY = (By.CSS_SELECTOR, '.react-datepicker__day--today')
    DELIVERY_PERIOD_DROPDOWN = (By.XPATH, "//div[@class = 'Dropdown-placeholder' and text() = '* Срок аренды']")
    DELIVERY_PERIOD = (By.XPATH, "//div[@class = 'Dropdown-option' and text() = 'сутки']")
    BUTTON_ORDER = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM'and text()='Заказать']")
    BUTTON_YES = (By.XPATH, "//button[text() = 'Да']")
    STATUS_ORDER = (By.XPATH, "//div[text() = 'Заказ оформлен']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы Яндекс.Самокат')
    def open_page(self):
        self.open_url(UrlScooter.URL_LOGIN)

    @allure.step('Заполнить поле Имя')
    def click_name(self):
        name_input = self.wait_and_find_element(self.LOGIN_NAME)
        name_input.send_keys('Ольга')

    @allure.step('Заполнить поле Фамилия')
    def click_last_name(self):
        last_name_input = self.wait_and_find_element(self.LOGIN_LAST_NAME)
        last_name_input.send_keys('Терехова')

    @allure.step('Заполнить поле Адрес')
    def click_address(self):
        address_input = self.wait_and_find_element(self.LOGIN_ADDRESS)
        address_input.send_keys('Софийская, 8')

    @allure.step('Клик на станцию метро')
    def click_metrostation(self):
        metrostation = self.wait_and_find_element(self.METRO_STATION)
        metrostation.click()

    @allure.step('Выбрать станцию метро из выпадающего списка')
    def click_station(self):
        station = self.wait_and_find_element(self.STATION)
        station.click()

    @allure.step('Заполнить поле Телефон')
    def click_phone(self):
        phone_input = self.wait_and_find_element(self.PHONE)
        phone_input.send_keys('+79819467999')

    @allure.step('Клик на кнопку Далее')
    def click_next(self):
        next = self.wait_and_find_element(self.BUTTON_NEXT)
        next.click()

    @allure.step('Клик на Когда привезти самокат')
    def click_delivery(self):
        delivery = self.wait_and_find_element(self.DELIVERY)
        delivery.click()

    @allure.step('Когда привезти самокат: выбрать день')
    def click_delivery_day(self):
        delivery_day = self.wait_and_find_element(self.DELIVERY_DAY)
        delivery_day.click()

    @allure.step('Клик на выпадающий список срока аренды')
    def click_delivery_period_dropdown(self):
        delivery_period_dropdown = self.wait_and_find_element(self.DELIVERY_PERIOD_DROPDOWN)
        delivery_period_dropdown.click()

    @allure.step('Клик на срок аренды')
    def click_delivery_period(self):
        delivery_period = self.wait_and_find_element(self.DELIVERY_PERIOD)
        delivery_period.click()

    @allure.step('Клик на кнопку Заказать')
    def click_button_order(self):
        button_order = self.wait_and_find_element(self.BUTTON_ORDER)
        button_order.click()

    @allure.step('Клик на кнопку Да')
    def click_button_yes(self):
        button_yes = self.wait_and_find_element(self.BUTTON_YES)
        button_yes.click()

    @allure.step('Получение статуса Заказ оформлен')
    def get_status_order(self):
        return self.wait_and_find_element(self.STATUS_ORDER)
