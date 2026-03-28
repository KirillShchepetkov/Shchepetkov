import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com")
wait = WebDriverWait(driver, 15)

# 1. Логин, поиск поля
Login_field = ("xpath", "//input[@data-test='username']")

# 2. Ожидание, очистка и ввод логина
wait.until(EC.presence_of_element_located(Login_field)).clear()
wait.until(EC.presence_of_element_located(Login_field)).send_keys("standard_user")

# 3. Пароль, поиск поля
Password_Field = ("xpath", "//input[@data-test='password']")

# 4. Ожидание, очистка и ввод пароля
wait.until(EC.presence_of_element_located(Password_Field)).clear()
wait.until(EC.presence_of_element_located(Password_Field)).send_keys("secret_sauce")

# 5.Поиск кнопки и клик Login
Login_button = ("xpath", "//input[@data-test='login-button']")
wait.until(EC.element_to_be_clickable(Login_button)).click()

# 6.Ассерт на нужный Урл
assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Неправильный URL"

# 7.Выбираем рюкзак
Backpack = ("xpath", "//button[@data-test='add-to-cart-sauce-labs-backpack']")
wait.until(EC.element_to_be_clickable(Backpack)).click()



time.sleep(6)





