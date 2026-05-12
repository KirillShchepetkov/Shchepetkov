# pages/checkout_page.py
import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class CheckoutPage(BasePage):
    """Страница оформления заказа"""

    # Локаторы для шага 1
    _FIRST_NAME_INPUT = (By.XPATH, "//input[@name='firstName']")
    _LAST_NAME_INPUT = (By.XPATH, "//input[@name='lastName']")
    _POSTAL_CODE_INPUT = (By.XPATH, "//input[@name='postalCode']")
    _CONTINUE_BUTTON = (By.XPATH, "//input[@data-test='continue']")
    _ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    # Локаторы для шага 2
    _FINISH_BUTTON = (By.XPATH, "//button[@data-test='finish']")
    _CANCEL_BUTTON = (By.XPATH, "//button[@data-test='cancel']")

    # Локаторы для завершения
    _COMPLETE_HEADER = (By.XPATH, "//h2[@data-test='complete-header']")
    _BACK_HOME_BUTTON = (By.XPATH, "//button[@data-test='back-to-products']")

    @allure.step("Enter shipping information")
    def enter_shipping_info(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        """Ввести данные для доставки (шаг 1)"""
        self.type_text(self._FIRST_NAME_INPUT, first_name)
        self.type_text(self._LAST_NAME_INPUT, last_name)
        self.type_text(self._POSTAL_CODE_INPUT, postal_code)
        self.attach_screenshot("shipping_info_entered")
        return self

    @allure.step("Click continue button")
    def click_continue(self) -> 'CheckoutPage':
        """Нажать continue (переход к шагу 2)"""
        self.click(self._CONTINUE_BUTTON)
        self.attach_screenshot("checkout_step_two")
        return self

    @allure.step("Click finish button")
    def click_finish(self) -> 'CheckoutPage':
        """Нажать finish (завершение покупки)"""
        self.click(self._FINISH_BUTTON)
        self.attach_screenshot("purchase_completed")
        return self

    @allure.step("Back to products")
    def back_to_products(self) -> 'InventoryPage':
        """Вернуться к товарам"""
        from pages.inventory_page import InventoryPage
        self.click(self._BACK_HOME_BUTTON)
        return InventoryPage(self.driver)

    @allure.step("Get error message")
    def get_error_message(self) -> str:
        """Получить сообщение об ошибке"""
        if self.is_element_visible(self._ERROR_MESSAGE):
            return self.get_text(self._ERROR_MESSAGE)
        return ""

    @allure.step("Get complete message")
    def get_complete_message(self) -> str:
        """Получить сообщение об успешном завершении"""
        if self.is_element_visible(self._COMPLETE_HEADER):
            return self.get_text(self._COMPLETE_HEADER)
        return ""

    def is_checkout_complete(self) -> bool:
        """Проверить завершение оформления"""
        return "checkout-complete.html" in self.get_current_url()