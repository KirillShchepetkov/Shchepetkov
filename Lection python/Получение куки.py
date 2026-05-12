import json
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://stagingpartner.strana.com/lk/trading")

input()

cookies = driver.get_cookies()
with open('cookies.json', 'w') as file:
    json.dump(cookies, file, indent=4)

    # Получение куки










