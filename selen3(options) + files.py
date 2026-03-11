import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://staging.sso.strana.com/realms/strana/protocol/openid-connect/auth?client_id=partners&redirect_uri=https%3A%2F%2Fstagingpartner.strana.com%2Flk%2Ftrading&state=c2934501-50de-4617-9d2f-c72a1a0bb8fe&response_mode=fragment&response_type=code&scope=openid&nonce=79a31bf5-d356-44a3-8490-01a5acef06ed&code_challenge=ctmlHjsgOkgzWpD2mOLfhC1kQio4lwWpchH3AtTGCws&code_challenge_method=S256")
wait = WebDriverWait(driver, 10)
username_field = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )

INPUT_FIELD = ("xpath", "//input[@id='username']")
driver.find_element(*INPUT_FIELD).send_keys("0000000070@ya.ru")
time.sleep(2)

INPUT_FIELD = ("xpath", "//input[@id='password']")
driver.find_element(*INPUT_FIELD).send_keys("tZq-WvH-NKp-x4B")
time.sleep(2)

INPUT_FIELD = ("xpath", "//div[@id='kc-form-buttons']/button")
driver.find_element(*INPUT_FIELD).send_keys(Keys.ENTER)
time.sleep(4)

INPUT_FIELD = ("xpath", "//button[contains(@class, 'button__primary') and contains(@class, 'kc-b-trading-list__create-btn')]")
driver.find_element(*INPUT_FIELD).send_keys(Keys.ENTER)
time.sleep(4)

INPUT_FIELD = ("xpath", "//button[.//span[text()='Процедура по СМР']]")
driver.find_element(*INPUT_FIELD).send_keys(Keys.ENTER)
time.sleep(4)

INPUT_FIELD = ("xpath", "//div[contains(@class, 'content-part_4d929')]//textarea")
driver.find_element(*INPUT_FIELD).send_keys("1 автотест")
time.sleep(4)

driver.execute_script("arguments[0].value = '20.03.26';", driver.find_elements(By.XPATH, "//input[@placeholder='ДД.ММ.ГГ']")[1])
time.sleep(4)

driver.execute_script("arguments[0].value = '19:00';", driver.find_elements(By.XPATH, "//input[@placeholder='ЧЧ.ММ']")[1])
time.sleep(4)



