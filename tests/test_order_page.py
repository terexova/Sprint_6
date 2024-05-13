import allure

from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    def perform_test(self, driver, option=0):
        main_page = MainPage(driver)
        main_page.open_page()
        if option != 0:
            main_page.scroll_page()
            main_page.click_order_down()
        else:
            main_page.click_order_up()

        order_page = OrderPage(driver, option)
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

        return order_page.wait_and_find_element(order_page.STATUS_ORDER)



    @allure.title('Проверка: позитивный сценарий регистрации через кнопку «Заказать» вверху страницы')
    @allure.description('Клик на вопрос и проверяем ответ')
    def test_success_order_1(self, driver):
        status = self.perform_test(driver, 0)
        assert status.is_displayed()

    @allure.title('Проверка: позитивный сценарий регистрации через кнопку «Заказать» внизу страницы')
    @allure.description('Клик на вопрос и проверяем ответ')
    def test_success_order_2(self, driver):
        status = self.perform_test(driver, 1)
        assert status.is_displayed()