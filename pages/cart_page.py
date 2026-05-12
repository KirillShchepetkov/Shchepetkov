# pages/cart_page.py
import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    """Страница корзины"""

    # Локаторы
    _CART_ITEM = (By.CLASS_NAME, "cart_item")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.XPATH, "//button[@data-test='checkout']")
    _CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[@data-test='continue-shopping']")

    @allure.step("Get cart items count")
    def get_cart_items_count(self) -> int:
        """Получить количество товаров в корзине"""
        items = self.get_elements(self._CART_ITEM)
        return len(items)

    @allure.step("Get product names in cart")
    def get_product_names(self) -> list:
        """Получить названия товаров в корзине"""
        products = self.get_elements(self._PRODUCT_NAME)
        return [product.text for product in products]

    @allure.step("Proceed to checkout")
    def proceed_to_checkout(self) -> CheckoutPage:
        """Перейти к оформлению заказа"""
        self.click(self._CHECKOUT_BUTTON)
        self.attach_screenshot("checkout_step_one")
        return CheckoutPage(self.driver)

    @allure.step("Continue shopping")
    def continue_shopping(self) -> 'InventoryPage':
        """Вернуться к покупкам"""
        from pages.inventory_page import InventoryPage
        self.click(self._CONTINUE_SHOPPING_BUTTON)
        return InventoryPage(self.driver)

    def is_cart_displayed(self) -> bool:
        """Проверить отображение страницы корзины"""
        return "cart.html" in self.get_current_url()