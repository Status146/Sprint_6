from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    LAST_NAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_FIELD = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    STATION_1 = By.XPATH, "//li[@class='select-search__row' and @data-index='1' and @data-value='2']"
    STATION_2 = By.XPATH, "//li[@class='select-search__row' and @data-index='5' and @data-value='6']"
    PHONE_FIELD = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"
    DATE_FIELD = By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"
    DATE_1 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--019']"
    DATE_2 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--004']"
    RENT_FIELD = By.XPATH, "//div[text()='* Срок аренды']"
    TERM_1 = By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"
    TERM_2 = By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']"
    BLACK_COLOR = By.ID, "black"
    GREY_COLOR = By.ID, "grey"
    COMMENTS = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    YES_BUTTON = By.XPATH, "//button[text()='Да']"
    ORDER_SUCCESS_WINDOW = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"

