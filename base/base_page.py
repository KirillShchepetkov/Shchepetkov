import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from typing import List, Tuple


class BasePage:
    """Базовый класс для всех страниц с общими методами"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5)

    def open(self, url: str):
        """Открыть URL"""
        with allure.step(f"Open page: {url}"):
            self.driver.get(url)

    def find_element(self, locator: Tuple[By, str], timeout: int = 10) -> WebElement:
        """Найти элемент с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: Tuple[By, str]):
        """Кликнуть по элементу"""
        with allure.step(f"Click on element: {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

    def type_text(self, locator: Tuple[By, str], text: str):
        """Ввести текст в поле"""
        with allure.step(f"Type text: '{text}'"):
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)

    def get_text(self, locator: Tuple[By, str]) -> str:
        """Получить текст элемента"""
        return self.find_element(locator).text

    def is_element_present(self, locator: Tuple[By, str], timeout: int = 3) -> bool:
        """Проверить наличие элемента на странице"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    def is_element_visible(self, locator: Tuple[By, str], timeout: int = 3) -> bool:
        """Проверить видимость элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def get_elements(self, locator: Tuple[By, str]) -> List[WebElement]:
        """Найти все элементы по локатору"""
        return self.driver.find_elements(*locator)

    def attach_screenshot(self, name: str = "screenshot"):
        """Прикрепить скриншот к Allure отчету"""
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG
        )

    def get_current_url(self) -> str:
        """Получить текущий URL"""
        return self.driver.current_url

    def wait_for_url_contains(self, text: str, timeout: int = 10):
        """Ожидать, что URL содержит указанный текст"""
        self.wait.until(lambda driver: text in driver.current_url)