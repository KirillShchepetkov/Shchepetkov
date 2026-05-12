import time
import json
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://stagingpartner.strana.com/lk/trading")

driver.delete_all_cookies()

with open("cookies.json", "r") as file:
    cookies = json.load(file)
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)