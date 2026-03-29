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


# 8.Выбираем фонарь велосипеда
Bike_light = ("xpath", "//button[@data-test='add-to-cart-sauce-labs-bike-light']")
wait.until(EC.element_to_be_clickable(Bike_light)).click()

# 9.Выбираем красную кофту
Red_t_shirt = ("xpath", "//button[@data-test='add-to-cart-test.allthethings()-t-shirt-(red)']")
wait.until(EC.element_to_be_clickable(Red_t_shirt)).click()

# 10.Проваливаемся в корзину
Cart_link = ("xpath", "//a[@data-test='shopping-cart-link']")
wait.until(EC.element_to_be_clickable(Cart_link)).click()


# 11.Ассерт на нужный Урл корзины
assert driver.current_url == "https://www.saucedemo.com/cart.html", "Неправильный URL корзины"


# 12.Прожимаем  чекаут
Checkout = ("xpath", "//button[@data-test='checkout']")
wait.until(EC.element_to_be_clickable(Checkout)).click()

# 13.Ассерт на нужный Урл чекаут
assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Неправильный URL чекаут"

# 14.Заполнение Имени, Фамилии, Кода
First_name = ("xpath", "//input[@data-test='firstName']")
wait.until(EC.presence_of_element_located(First_name)).clear()
wait.until(EC.presence_of_element_located(First_name)).send_keys("Kirill")


Last_Name = ("xpath", "//input[@data-test='lastName']")
wait.until(EC.presence_of_element_located(Last_Name)).clear()
wait.until(EC.presence_of_element_located(Last_Name)).send_keys("Shchepetkov")


Postal_Code = ("xpath", "//input[@data-test='postalCode']")
wait.until(EC.presence_of_element_located(Postal_Code)).clear()
wait.until(EC.presence_of_element_located(Postal_Code)).send_keys("4712")

# 15.Прожимаем continue
Сontinue_click = 

time.sleep(7)
