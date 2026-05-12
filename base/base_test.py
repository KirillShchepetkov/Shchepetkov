import pytest
import allure
from config.credentials import credentials
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
# from utiles.generator import Generators

class BaseTest:
    """Базовый класс для всех тестов с общими методами"""

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        """Инициализация всех страниц для тестов"""
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
        # self.generator = Generators()

    # ========== Методы для авторизации ==========

    @allure.step("Login as standard user")
    def login_as_standard_user(self) -> InventoryPage:
        """Логин под стандартным пользователем"""
        username, password = credentials.get_sauce_user("standard")
        return (self.login_page
                .open_page()
                .login(username, password))

    @allure.step("Login as locked user")
    def login_as_locked_user(self) -> LoginPage:
        """Попытка логина заблокированным пользователем"""
        username, password = credentials.get_sauce_user("locked")
        self.login_page.open_page()
        return self.login_page.login(username, password)

    @allure.step("Login as problem user")
    def login_as_problem_user(self) -> InventoryPage:
        """Логин под проблемным пользователем"""
        username, password = credentials.get_sauce_user("problem")
        return (self.login_page
                .open_page()
                .login(username, password))

    # ========== Методы для подготовки данных ==========

    @allure.step("Login and add product to cart")
    def login_and_add_product(self) -> InventoryPage:
        """Логин и добавление товара в корзину"""
        inventory_page = self.login_as_standard_user()
        inventory_page.add_product_to_cart()
        self.attach_screenshot("product_added_to_cart")
        return inventory_page

    @allure.step("Login and go to cart")
    def login_and_go_to_cart(self) -> CartPage:
        """Логин и переход в корзину"""
        inventory_page = self.login_as_standard_user()
        inventory_page.add_product_to_cart()
        return inventory_page.open_cart()

    @allure.step("Login and go to checkout")
    def login_and_go_to_checkout(self) -> CheckoutPage:
        """Логин, добавление товара и переход к оформлению"""
        cart_page = self.login_and_go_to_cart()
        return cart_page.proceed_to_checkout()

    @allure.step("Complete full purchase")
    def complete_full_purchase(self, first_name: str = "Test",
                               last_name: str = "User",
                               postal_code: str = "12345") -> InventoryPage:
        """Выполнить полный цикл покупки"""
        checkout_page = self.login_and_go_to_checkout()
        return (checkout_page
                .enter_shipping_info(first_name, last_name, postal_code)
                .click_continue()
                .click_finish()
                .back_to_products())

    # ========== Вспомогательные методы ==========

    @allure.step("Attach screenshot to report")
    def attach_screenshot(self, name: str = "screenshot"):
        """Прикрепить скриншот к Allure отчету"""
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def get_environment_info(self) -> dict:
        """Получить информацию об окружении"""
        import os
        return {
            "STAGE": os.getenv("STAGE", "unknown"),
            "BROWSER": os.getenv("BROWSER", "unknown")
        }


