import allure

from conftest import driver
from data import UrlScooter
from data import UrlDzen
from pages.main_page import MainPage


class TestLogo:

    @allure.title('Проверка: логотип Самокат')
    @allure.description('Клик на логотип Самокат ведет на сайт Яндекс.Самокат')
    def test_logo_Scooter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_order_up()
        main_page.click_logo_Scooter()

        assert main_page.get_current_url() == UrlScooter.URL

    @allure.title('Проверка: логотип Яндекс')
    @allure.description('Клик на логотип Яндекс ведет на сайт Дзена')
    def test_logo_Yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_logo_Yandex_and_go()
        main_page.wait_url_to_be(UrlDzen.URL)

        assert main_page.get_current_url() == UrlDzen.URL
