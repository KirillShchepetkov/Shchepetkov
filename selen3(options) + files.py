import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Настройки Chrome для стабильности
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.get("https://staging.sso.strana.com/realms/strana/protocol/openid-connect/auth?client_id=partners&redirect_uri=https%3A%2F%2Fstagingpartner.strana.com%2Flk%2Ftrading&state=c2934501-50de-4617-9d2f-c72a1a0bb8fe&response_mode=fragment&response_type=code&scope=openid&nonce=79a31bf5-d356-44a3-8490-01a5acef06ed&code_challenge=ctmlHjsgOkgzWpD2mOLfhC1kQio4lwWpchH3AtTGCws&code_challenge_method=S256")
wait = WebDriverWait(driver, 15)

# === АВТОРИЗАЦИЯ ===
LOGIN_FIELD = ("xpath", "//input[@id='username']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//div[@id='kc-form-buttons']/button")

wait.until(EC.presence_of_element_located(LOGIN_FIELD)).send_keys("0000000070@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("tZq-WvH-NKp-x4B")
driver.find_element(*SUBMIT_BUTTON).send_keys(Keys.ENTER)
time.sleep(3)

# === СОЗДАНИЕ ПРОЦЕДУРЫ ===
CREATE_PROC_BUTTON = ("xpath", "//button[contains(@class, 'button__primary') and contains(@class, 'kc-b-trading-list__create-btn')]")
SMR_PROC_BUTTON = ("xpath", "//button[.//span[text()='Процедура по СМР']]")

wait.until(EC.element_to_be_clickable(CREATE_PROC_BUTTON)).send_keys(Keys.ENTER)
time.sleep(2)

wait.until(EC.element_to_be_clickable(SMR_PROC_BUTTON)).send_keys(Keys.ENTER)
time.sleep(2)

# === НАИМЕНОВАНИЕ ===
NAME_FIELD = ("xpath", "//div[contains(@class, 'content-part_4d929')]//textarea")
wait.until(EC.presence_of_element_located(NAME_FIELD)).send_keys("1 автотест")
time.sleep(2)

# === СКРОЛЛ К ДАТЕ ===
DATE_PLACEHOLDER = ("xpath", "//input[@placeholder='ДД.ММ.ГГ']")
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(*DATE_PLACEHOLDER))
time.sleep(1)

# === КОММЕНТАРИЙ ===
COMMENT_EDITOR = ("css selector", ".ql-editor")
editor = driver.find_elements(*COMMENT_EDITOR)[0]
driver.execute_script("arguments[0].innerHTML = '<p>1 коммент</p>';", editor)
print("✅ Комментарий введён")
time.sleep(3)

# === ВЫБОР ДАТЫ ОКОНЧАНИЯ ПОДАЧИ ЗАЯВОК ===
print("🔍 Выбор даты окончания подачи заявок...")

DATE_FIELD = ("xpath", "//input[@placeholder='ДД.ММ.ГГ']")
driver.find_elements(*DATE_FIELD)[1].click()
time.sleep(1)

DATE_BUTTON = ("xpath", "//button[.//abbr[@aria-label='20 марта 2026 г.']]")
wait.until(EC.element_to_be_clickable(DATE_BUTTON)).click()
print("✅ Выбрана дата: 20 марта 2026")
time.sleep(1)

# === ВЫБОР ВРЕМЕНИ ===
print("🔍 Выбор времени...")

TIME_FIELD = ("xpath", "//input[@placeholder='ЧЧ.ММ']")
time_field = driver.find_elements(*TIME_FIELD)[1]
time_field.click()
time.sleep(1)
time_field.clear()
time_field.send_keys("19:00")
time_field.send_keys(Keys.ENTER)
print("✅ Время 19:00 введено")
time.sleep(1)

# === ВЫБОР СРОКОВ ПРОВЕДЕНИЯ РАБОТ ===
print("🔍 Выбор сроков проведения работ...")

PERIOD_FIELD = ("xpath", "//input[@placeholder='ДД.ММ.ГГГГ – ДД.ММ.ГГГГ']")
driver.find_elements(*PERIOD_FIELD)[0].click()
time.sleep(2)

START_DATE = ("xpath", "//button[contains(@class, 'react-calendar__tile') and .//abbr[text()='21']]")
driver.execute_script("arguments[0].click();", driver.find_element(*START_DATE))
time.sleep(1)

END_DATE = ("xpath", "//button[contains(@class, 'react-calendar__tile') and .//abbr[text()='22']]")
driver.execute_script("arguments[0].click();", driver.find_element(*END_DATE))
print("✅ Выбрана дата: 21.03.2026 — 22.03.2026")
time.sleep(2)

# === КНОПКА "СЛЕДУЮЩИЙ ШАГ" ===
NEXT_STEP_BUTTON = ("xpath", "//button[.//span[text()='Следующий шаг']]")
next_btn = wait.until(EC.presence_of_element_located(NEXT_STEP_BUTTON))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", next_btn)
print("✅ Кнопка нажата")
time.sleep(4)

driver.quit()