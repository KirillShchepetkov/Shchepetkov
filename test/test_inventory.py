
import pytest
import allure
from allure_commons.types import Severity
from base.base_test import BaseTest


@allure.epic("Store")
@allure.feature("Inventory")
@pytest.mark.regression
class TestInventory(BaseTest):

    @allure.title("Add product to cart")
    @allure.severity(Severity.CRITICAL)
    def test_add_product_to_cart(self):
        """Тест добавления товара в корзину"""
        self.login_as_standard_user()
        self.inventory_page.add_product_to_cart()

        assert self.inventory_page.get_cart_count() == 1
        self.attach_screenshot("product_added")

        cart_page = self.inventory_page.open_cart()
        assert cart_page.get_cart_items_count() == 1
        assert "Sauce Labs Backpack" in cart_page.get_product_names()

    @allure.title("Cart badge displays correct count")
    @allure.severity(Severity.NORMAL)
    def test_cart_badge_count(self):
        """Тест счетчика корзины"""
        self.login_as_standard_user()

        self.inventory_page.add_product_to_cart()
        assert self.inventory_page.get_cart_count() == 1
        self.attach_screenshot("cart_badge_count_1")

        self.inventory_page.remove_product_from_cart()
        assert self.inventory_page.get_cart_count() == 0
        self.attach_screenshot("cart_badge_count_0")

    @allure.title("Add Sauce Labs Bike Light to cart")
    @allure.severity(Severity.NORMAL)
    def test_add_bike_light_to_cart(self):
        """Тест добавления Bike Light в корзину"""
        self.login_as_standard_user()
        self.inventory_page.add_bike_light_to_cart()

        assert self.inventory_page.get_cart_count() == 1
        self.attach_screenshot("bike_light_cart")

        cart_page = self.inventory_page.open_cart()
        assert "Sauce Labs Bike Light" in cart_page.get_product_names()

    @allure.title("Add Sauce Labs Onesie to cart")
    @allure.severity(Severity.NORMAL)
    def test_add_onesie_to_cart(self):
         """Тест добавления Sauce Labs Onesie в корзину"""
         self.login_as_standard_user()
         self.inventory_page.add_onesie_to_cart()

         assert self.inventory_page.get_cart_count() == 1
         self.attach_screenshot("onesie_to_cart")

         cart_page = self.inventory_page.open_cart()
         assert "Sauce Labs Onesie" in cart_page.get_product_names()
