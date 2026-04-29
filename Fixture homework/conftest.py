import os # импорт модуля для работы с ос (переменные окружения, файлы-пути)
import pytest # импорт библиотеки для фикстур
from selenium import webdriver # импорт вебдрайвера
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
def open_saucedemo(request):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def Login_saucedemo(request):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com")
    driver.find_element("xpath", "//input[@placeholder='Username']").send_keys("standard_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@name='login-button']").click()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def Checkout_saucedemo(request):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com")

    # Сначала авторизуемся
    driver.find_element("xpath", "//input[@placeholder='Username']").send_keys("standard_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@name='login-button']").click()

    # Теперь добавляем товар в корзину
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
    )
    driver.find_element("xpath", "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element("xpath", "//*[@data-test='shopping-cart-link']").click()
    driver.find_element("xpath", "//button[@data-test='checkout']").click()

    request.cls.driver = driver
    yield
    driver.quit()


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