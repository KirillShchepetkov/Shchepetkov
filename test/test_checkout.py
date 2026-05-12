
import pytest
import allure
from allure_commons.types import Severity
from base.base_test import BaseTest


@allure.epic("Purchase")
@allure.feature("Checkout")
@pytest.mark.regression
class TestCheckout(BaseTest):

    @allure.title("Complete full purchase workflow")
    @allure.severity(Severity.CRITICAL)
    def test_complete_purchase(self):
        """Тест полного цикла покупки"""
        inventory_page = self.complete_full_purchase(
            first_name="Kirill",
            last_name="Shchepetkov",
            postal_code="123456"
        )

        assert inventory_page.is_inventory_displayed()
        self.attach_screenshot("purchase_completed")

    @allure.title("Checkout with empty fields shows error")
    @allure.severity(Severity.NORMAL)
    def test_checkout_empty_fields_error(self):
        """Тест оформления с пустыми полями"""
        checkout_page = self.login_and_go_to_checkout()

        checkout_page.click_continue()

        assert "First Name is required" in checkout_page.get_error_message()
        self.attach_screenshot("checkout_empty_fields_error")

    @allure.title("Checkout with partial data")
    @allure.severity(Severity.NORMAL)
    def test_checkout_partial_data(self):
        """Тест оформления с частично заполненными данными"""
        checkout_page = self.login_and_go_to_checkout()

        checkout_page.enter_shipping_info("Kirill", "", "")
        checkout_page.click_continue()

        assert "Last Name is required" in checkout_page.get_error_message()
        self.attach_screenshot("checkout_missing_lastname")