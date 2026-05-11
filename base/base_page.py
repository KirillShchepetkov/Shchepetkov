import allure
from selenium.webdriver.remote.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator

class BasePage(metaclass=MetaLocator):

    _LOGO = "//a[contains(@class, 'navabar-brand')]"

    def __init__(self, driver):
        self.driver: WebDriver = driver


    def open(self):
        with allure.step(f"Open {self._PAGE_URL} page"):
            self.driver.get(self._PAGE_URL)