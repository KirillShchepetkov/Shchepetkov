# config/credentials.py
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


@dataclass
class SauceDemoCredentials:
    """Учетные данные для SauceDemo"""
    standard_user: str
    locked_out_user: str
    problem_user: str
    password: str


class CredentialsManager:
    """Менеджер для работы с учетными данными"""

    @property
    def saucedemo(self) -> SauceDemoCredentials:
        return SauceDemoCredentials(
            standard_user=os.getenv("SAUCE_USERNAME_STANDARD", "standard_user"),
            locked_out_user=os.getenv("SAUCE_USERNAME_LOCKED", "locked_out_user"),
            problem_user=os.getenv("SAUCE_USERNAME_PROBLEM", "problem_user"),
            password=os.getenv("SAUCE_PASSWORD", "secret_sauce")
        )

    def get_sauce_user(self, user_type: str = "standard") -> tuple[str, str]:
        """Получить пару (username, password) для SauceDemo"""
        users = {
            "standard": (self.saucedemo.standard_user, self.saucedemo.password),
            "locked": (self.saucedemo.locked_out_user, self.saucedemo.password),
            "problem": (self.saucedemo.problem_user, self.saucedemo.password),
        }
        return users.get(user_type, users["standard"])


credentials = CredentialsManager()