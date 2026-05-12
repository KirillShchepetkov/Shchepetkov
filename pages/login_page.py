# pages/login_page.py
import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    """Страница авторизации SauceDemo"""

    # Локаторы
    _USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Username']")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.NAME, "login-button")
    _ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com"

    @allure.step("Open login page")
    def open_page(self) -> 'LoginPage':
        """Открыть страницу логина"""
        self.open(self.url)
        self.attach_screenshot("login_page_opened")
        return self

    @allure.step("Enter username: {username}")
    def enter_username(self, username: str) -> 'LoginPage':
        """Ввести имя пользователя"""
        self.type_text(self._USERNAME_INPUT, username)
        return self

    @allure.step("Enter password")
    def enter_password(self, password: str) -> 'LoginPage':
        """Ввести пароль"""
        self.type_text(self._PASSWORD_INPUT, password)
        return self

    @allure.step("Click login button")
    def click_login_button(self) -> InventoryPage:
        """Нажать кнопку логина"""
        self.click(self._LOGIN_BUTTON)
        self.attach_screenshot("after_login_click")
        return InventoryPage(self.driver)

    @allure.step("Login with credentials")
    def login(self, username: str, password: str) -> InventoryPage:
        """Выполнить авторизацию"""
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login_button()

    @allure.step("Get error message")
    def get_error_message(self) -> str:
        """Получить текст сообщения об ошибке"""
        if self.is_element_visible(self._ERROR_MESSAGE):
            return self.get_text(self._ERROR_MESSAGE)
        return ""

    def is_error_displayed(self) -> bool:
        """Проверить наличие ошибки"""
        return self.is_element_visible(self._ERROR_MESSAGE)