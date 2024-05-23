import allure

from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка: позитивный сценарий регистрации через кнопку «Заказать» вверху страницы')
    @allure.description('Клик на вопрос и проверяем ответ')
    def test_success_order_up(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_order_up()

        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.click_name()

        order_page.click_last_name()
        order_page.click_address()
        order_page.click_metrostation()
        order_page.click_station()
        order_page.click_phone()
        order_page.click_next()

        order_page.click_delivery()
        order_page.click_delivery_day()
        order_page.click_delivery_period_dropdown()
        order_page.click_delivery_period()
        order_page.click_button_order()

        order_page.click_button_yes()

        assert order_page.get_status_order()

    @allure.title('Проверка: позитивный сценарий регистрации через кнопку «Заказать» внизу страницы')
    @allure.description('Клик на вопрос и проверяем ответ')
    def test_success_order_down(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_cookie()
        main_page.click_order_down()

        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.click_name()

        order_page.click_last_name()
        order_page.click_address()
        order_page.click_metrostation()
        order_page.click_station()
        order_page.click_phone()
        order_page.click_next()

        order_page.click_delivery()
        order_page.click_delivery_day()
        order_page.click_delivery_period_dropdown()
        order_page.click_delivery_period()
        order_page.click_button_order()

        order_page.click_button_yes()

        assert order_page.get_status_order()