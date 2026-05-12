# pages/inventory_page.py
import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):
    """Страница с товарами после логина"""

    # Локаторы
    _INVENTORY_CONTAINER = (By.XPATH, "//div[@data-test='inventory-container']")
    _ADD_TO_CART_BUTTON = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    _REMOVE_BUTTON = (By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.XPATH, "//*[@data-test='shopping-cart-link']")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Add product to cart")
    def add_product_to_cart(self) -> 'InventoryPage':
        """Добавить товар в корзину"""
        if self.is_element_visible(self._ADD_TO_CART_BUTTON):
            self.click(self._ADD_TO_CART_BUTTON)
            self.attach_screenshot("product_added_to_cart")
        return self

    @allure.step("Remove product from cart")
    def remove_product_from_cart(self) -> 'InventoryPage':
        """Удалить товар из корзины"""
        if self.is_element_visible(self._REMOVE_BUTTON):
            self.click(self._REMOVE_BUTTON)
            self.attach_screenshot("product_removed_from_cart")
        return self

    @allure.step("Get cart items count")
    def get_cart_count(self) -> int:
        """Получить количество товаров в корзине"""
        if self.is_element_visible(self._CART_BADGE):
            return int(self.get_text(self._CART_BADGE))
        return 0

    @allure.step("Open cart")
    def open_cart(self) -> CartPage:
        """Открыть корзину"""
        self.click(self._CART_LINK)
        self.attach_screenshot("cart_opened")
        return CartPage(self.driver)

    @allure.step("Get product names")
    def get_product_names(self) -> list:
        """Получить список названий товаров"""
        products = self.get_elements(self._PRODUCT_NAME)
        return [product.text for product in products]

    def is_inventory_displayed(self) -> bool:
        """Проверить отображение страницы инвентаря"""
        return self.is_element_visible(self._INVENTORY_CONTAINER)