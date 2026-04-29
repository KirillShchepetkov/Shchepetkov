import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import Severity

# pytest "Fixture homework/test_example.py" - запуск в терминале
# allure serve allure-results - получение отчета
# $env:STAGE="Stage 1.AQA";$env:BROWSER="Chrome";pytest "Fixture homework/test_example.py" - запуск с окружением

@allure.epic("Accounts")
@allure.feature("Login")
@allure.story("Pages")

@pytest.mark.smoke
class TestAuth:

    @pytest.mark.usefixtures("driver")
    @allure.title("Open login page")
    @allure.severity(Severity.CRITICAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_open_login_page(self):
        with allure.step("Open page. Step 1"):
            self.driver.get("https://www.saucedemo.com")

        with allure.step("Assert open page. Step 2"):
            assert self.driver.current_url == "https://www.saucedemo.com/", "Ошибка ULR страницы входа"
            allure.attach(
                body = self.driver.get_screenshot_as_png(),
                name = "Open login page",
                attachment_type= allure.attachment_type.PNG

            )

    @pytest.mark.usefixtures("open_saucedemo")
    @allure.title("open_saucedemo")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_open_books_page(self):
        with allure.step("Enter username. Step 3"):
            user_name = self.driver.find_element("xpath","//input[@data-test='username']")
            user_name.send_keys("standard_user")
        with allure.step("Enter password"):
            password_user = self.driver.find_element("xpath", "//input[@id='password']")
            password_user.send_keys("secret_sauce")
        with allure.step("Click login button"):
            button_auth = self.driver.find_element("xpath", "//input[@name = 'login-button']")
            button_auth.click()

            # ждем пока прогрузится картинка и тогда делаем скриншот
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@data-test='inventory-item-sauce-labs-backpack-img']"))
            )
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Авторизация успешна",
                attachment_type=AttachmentType.PNG
            )
        with allure.step("Assert redirect to inventory page"):
            assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Авторизация не выполнена"

    @pytest.mark.regression
    class TestInventory:
        @pytest.mark.usefixtures("Login_saucedemo")
        def test_inventory_login(self):
            with allure.step("Кликабельность кнопки добавления товара"):
                button_price = self.driver.find_element("xpath","//button[@data-test='add-to-cart-sauce-labs-backpack']")
                button_price.click()
            with allure.step("Проверка на изменение названия кнопки Remove"):
                remove_button = self.driver.find_elements("xpath", "//button[@data-test='remove-sauce-labs-backpack']")
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Кнопка изменила свое название",
                    attachment_type=AttachmentType.PNG
                )
                assert len(remove_button) > 0, "Кнопка не изменилась с Add-to-cart на Remove"
                assert remove_button[0].text == "Remove", f"Ожидался текст 'Remove', получено '{remove_button[0].text}'"

        @pytest.mark.usefixtures("Login_saucedemo")
        def test_cart_badge(self):
            with allure.step("Добавление одного товара"):
                self.driver.find_element("xpath", "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
            with allure.step("Значение счетчика корзины при добавлении 1-го товара"):
                cart_badge = self.driver.find_elements("class name", "shopping_cart_badge")
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Счетчик корзины",
                    attachment_type=AttachmentType.PNG
                )
                assert len(cart_badge) > 0, "Счетчик корзины отсутствует"
                assert cart_badge[0].text == "1", f"Ожидалось 1, получено {cart_badge[0].text}"

        @pytest.mark.usefixtures("Login_saucedemo")
        def test_cart_products(self):
            with allure.step("Добавление товара в корзину"):
                self.driver.find_element("xpath", "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Товар добавился",
                    attachment_type=AttachmentType.PNG
                )
            with allure.step("Переход в корзину"):
                self.driver.find_element("xpath", "//*[@data-test='shopping-cart-link']").click()
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Корзина с товаром",
                    attachment_type=AttachmentType.PNG
                )
                assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "Переход в корзину не отработал"
            with allure.step("Assert cart contains Sauce Labs Backpack"):
                cart_products = self.driver.find_elements("class name", "inventory_item_name")
                product_names = [product.text for product in cart_products]
                assert len(product_names) == 1, f"Ожидался 1 товар, найдено {len(product_names)}"
                assert product_names[
                           0] == "Sauce Labs Backpack", f"Ожидался 'Sauce Labs Backpack', найден '{product_names[0]}'"

    @pytest.mark.regression
    class TestCheckout:
        @pytest.mark.usefixtures("Checkout_saucedemo")
        def test_checkout_empty_fields(self):

            with allure.step("Click continue with empty fields"):
                self.driver.find_element("xpath", "//input[@data-test='continue']").click()
                # После нажатия continue без заполнения полей, мы остаемся на той же странице
                assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Осуществлен переход без вводимых данных"

            with allure.step("Assert error message displayed"):
                error_message = self.driver.find_elements("xpath", "//h3[@data-test='error']")
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Проверка на Assert error message",
                    attachment_type=AttachmentType.PNG
                )
                assert len(error_message) > 0, "Ошибка 'First Name is required' не появилась"
                assert error_message[
                           0].text == "Error: First Name is required", f"Ожидалось 'Error: First Name is required', получено '{error_message[0].text}'"

        @pytest.mark.usefixtures("Checkout_saucedemo")
        def test_full_purchase(self):

            with allure.step("Ввод данных"):
                self.driver.find_element("xpath", "//input[@name='firstName']").send_keys("Test")
                self.driver.find_element("xpath", "//input[@name='lastName']").send_keys("Testovsh")
                self.driver.find_element("xpath", "//input[@name='postalCode']").send_keys("320530")
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Заполненные инпуты с данными",
                    attachment_type=AttachmentType.PNG
                )

            with allure.step("Переход на шаг 2"):
                self.driver.find_element("xpath", "//input[@data-test='continue']").click()
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Переход на шаг 2",
                    attachment_type=AttachmentType.PNG
                )
                assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Переход на шаг 2 не осуществился"

            with allure.step("Финальный шаг"):
                self.driver.find_element("xpath", "//button[@data-test='finish']").click()
                assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "Переход на экран успешности не осуществлен"
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Покупка успешна",
                    attachment_type=AttachmentType.PNG
                )

            with allure.step("Возвращение на главный экран"):
                self.driver.find_element("xpath", "//button[@data-test='back-to-products']").click()
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Возвращение на главный экран",
                    attachment_type=AttachmentType.PNG
                )
                assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Переход на главный экран не осуществился"