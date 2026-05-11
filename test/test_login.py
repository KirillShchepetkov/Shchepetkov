import time
import allure
from base.base_test import BaseTest

@allure.epic("User")
@allure.feature("Login")
class TestLogin(BaseTest):


    @allure.step("Login in account")
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login("team1aqa@gmail.com")
        self.login_page.enter_password("qwerty")
        self.login_page.click_submit_button()
        self.dashboard_page.click_invite_button()
        time.sleep(5)
