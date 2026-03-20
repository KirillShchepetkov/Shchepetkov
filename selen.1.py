import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")

# Клик на кнопку, которая вызывает alert
driver.find_element("xpath", "//button[@id='alertButton']").click()

alert = wait.until(EC.alert_is_present())
time.sleep(3)
alert.dismiss()
time.sleep(3)
