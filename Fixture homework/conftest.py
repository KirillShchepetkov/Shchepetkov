import os # импорт модуля для работы с ос (переменные окружения, файлы-пути)
import pytest # импорт библиотеки для фикстур
from selenium import webdriver # импорт вебдрайвера
from selenium.webdriver.chrome.options import Options
# Костыль
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")  # убирает флаг автоматизации
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # убирает баннер "controlled by automated software"
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)

@pytest.fixture()
def driver(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(autouse=True)
def setup_environment_properties():
    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"]
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")