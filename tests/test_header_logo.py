from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from conftest import driver
from data import Urls
from locators.dzen_page_locators import DzenPageLocators
import allure


class TestHeaderLogo:
    @allure.title('Клик на лого Самоката в шапке возвращает на главную страницу')
    def test_redirect_samokat_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        main_page.click_samokat_logo()
        main_page.wait_navigating_url(Urls.main_page)
        assert main_page.find_element(MainPageLocators.ORDER_BUTTON_HEADER).is_displayed()

    @allure.title('Проверка редиректа на Dzen.ru при клике на Яндекс в лого шапки')
    def test_redirect_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_window(driver)
        main_page.wait_navigating_url(Urls.dzen_page)
        main_page.find_element(DzenPageLocators.DZEN_ICON)
        assert main_page.find_element(DzenPageLocators.DZEN_ICON).is_displayed()
