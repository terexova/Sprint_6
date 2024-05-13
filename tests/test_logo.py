import allure
import time

import data
from conftest import driver
from data import UrlScooter
from pages.main_page import MainPage


class TestLogo:

    @allure.title('Проверка: логотип Самокат')
    @allure.description('Клик на логотип Самокат ведет на сайт Яндекс.Самокат')
    def test_logo_Scooter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_order_up()
        main_page.click_logo_Scooter()

        assert driver.current_url == UrlScooter.URL

    @allure.title('Проверка: логотип Яндекс')
    @allure.description('Клик на логотип Яндекс ведет на сайт Дзена')
    def test_logo_Yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_logo_Yandex()

        time.sleep(10)
        driver.switch_to.window(driver.window_handles[-1])

        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
