import allure
from base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/ru/ru/login"
    _LOGIN_FIELD = "//input[@id='login_email']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _SUBMIT_BUTTON = "//button[@id='loginformsubmit']"

    @allure.step("Enter login")
    def enter_login(self, login):
        self.driver.find_element(By.XPATH, self._LOGIN_FIELD).send_keys(login)
        # Добавляем скриншот после ввода логина
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=f"Ввод логина: {login}",
            attachment_type=allure.attachment_type.PNG
        )


    @allure.step("Enter password")
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self. _PASSWORD_FIELD).send_keys(password)
        # Добавляем скриншот после ввода пароля
        allure.attach(
            self.driver.get_screenshot_as_png(),
            # показывает первые 2 символа пароля
            name=f"Password entered: {password[:2]}***",
            attachment_type=allure.attachment_type.PNG
        )


    @allure.step("Submit button")
    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self. _SUBMIT_BUTTON).click()
        # Добавляем скриншот после нажатия кнопки
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Submit button clicked",
            attachment_type=allure.attachment_type.PNG
        )