from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
# from utiles.generator import Generators

class BaseTest:

    def setup_method(self):
        # self.generator = Generators()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
