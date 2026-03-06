import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://staging.sso.strana.com/realms/strana/protocol/openid-connect/auth?client_id=partners&redirect_uri=https%3A%2F%2Fstagingpartner.strana.com%2Flk%2Ftrading&state=c2934501-50de-4617-9d2f-c72a1a0bb8fe&response_mode=fragment&response_type=code&scope=openid&nonce=79a31bf5-d356-44a3-8490-01a5acef06ed&code_challenge=ctmlHjsgOkgzWpD2mOLfhC1kQio4lwWpchH3AtTGCws&code_challenge_method=S256")
wait = WebDriverWait(driver, 5)
username_field = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )

INPUT_FIELD = ("xpath", "//input[@id='username']")
driver.find_element(*INPUT_FIELD).send_keys("r.asl@mail.ru")
assert username_field.get_attribute("value") == "r.asl@mail.ru", "❌ Логин неправильный"
time.sleep(2)

INPUT_FIELD = ("xpath", "//input[@id='password']")
driver.find_element(*INPUT_FIELD).send_keys("Qwe321!")
time.sleep(2)

INPUT_FIELD = ("xpath", "//div[@id='kc-form-buttons']/button")
driver.find_element(*INPUT_FIELD).send_keys(Keys.ENTER)
time.sleep(4)

# INPUT_FIELD = ("xpath", "//input[@data-testid='undefined-input']")
# driver.find_element(*INPUT_FIELD).send_keys("ЗП-0013603")
# time.sleep(7)