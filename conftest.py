import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Загружаем .env файл
load_dotenv()


@pytest.fixture(autouse=True)
def driver(request):
    """Фикстура для инициализации драйвера"""
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(autouse=True, scope="session")
def setup_environment_properties():
    """Создание environment.properties для Allure"""
    os.makedirs("allure-results", exist_ok=True)
    properties = {
        "STAGE": os.environ.get("STAGE", "default"),
        "BROWSER": os.environ.get("BROWSER", "Chrome"),
        "URL": "https://www.saucedemo.com"
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")