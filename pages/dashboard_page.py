import allure
from base.base_page import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/ru/ru/login"
    _INVITE_BUTTON = "//button[@title='Пригласить']"

    @allure.step("Click invite button")
    def click_invite_button(self):

        self.driver.find_element(By.XPATH, self._INVITE_BUTTON).click()