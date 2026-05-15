# tests/test_login.py
import pytest
import allure
from allure_commons.types import Severity
from base.base_test import BaseTest


@allure.epic("Accounts")
@allure.feature("Login")
@allure.story("Authentication")
@pytest.mark.smoke
class TestLogin(BaseTest):

    @allure.title("Successful login with standard user")
    @allure.severity(Severity.CRITICAL)
    def test_successful_login(self):
        """Тест успешного входа стандартным пользователем"""
        inventory_page = self.login_as_standard_user()

        assert inventory_page.is_inventory_displayed()
        assert inventory_page.get_current_url() == "https://www.saucedemo.com/inventory.html"
        self.attach_screenshot("successful_login")

    @allure.title("Login with locked out user shows error")
    @allure.severity(Severity.NORMAL)
    def test_locked_out_user_login(self):
        """Тест входа заблокированным пользователем"""
        self.login_as_locked_user()

        assert self.login_page.is_error_displayed()
        assert "locked out" in self.login_page.get_error_message().lower()
        self.attach_screenshot("locked_user_error")

    @allure.title("Login with problem user")
    @allure.severity(Severity.NORMAL)
    def test_problem_user_login(self):
        """Тест входа проблемным пользователем"""
        inventory_page = self.login_as_problem_user()

        assert inventory_page.is_inventory_displayed()
        self.attach_screenshot("problem_user_logged_in")

    @allure.title("Login with invalid credentials")
    @allure.severity(Severity.CRITICAL)
    def test_invalid_login(self):
        """Тест входа с неверными данными"""
        self.login_page.open_page()
        self.login_page.login("invalid_user", "wrong_password")

        assert self.login_page.is_error_displayed()
        assert "Username and password do not match" in self.login_page.get_error_message()
        self.attach_screenshot("invalid_login_error")


# Запуск всех тестов
# pytest test/ -v
#
# # Запуск конкретного теста
# pytest test/test_login.py -v
#
# # Запуск с Allure
# pytest test/ --alluredir=allure-results
# allure serve allure-results