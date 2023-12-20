from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from conftest import driver
from data import Urls
from locators.dzen_page_locators import DzenPageLocators
import allure


class TestHeaderLogo:
    @allure.title('Клик на лого Самоката в шапке возвращает на главную страницу')
    def test_redirect_samokat_logo(self, driver):
        MainPage(driver).click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        MainPage(driver).click_samokat_logo()
        MainPage(driver).wait_navigating_url(Urls.main_page)
        assert driver.find_element(*MainPageLocators.ORDER_BUTTON_HEADER).is_displayed()

    @allure.title('Проверка редиректа на Dzen.ru при клике на Яндекс в лого шапки')
    def test_redirect_yandex_logo(self, driver):
        MainPage(driver).click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        MainPage(driver).wait_navigating_url(Urls.dzen_page)
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(DzenPageLocators.SEARCH_BUTTON))
        assert driver.find_element(*DzenPageLocators.SEARCH_BUTTON).is_displayed()
