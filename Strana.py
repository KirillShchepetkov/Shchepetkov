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

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)

driver = webdriver.Chrome(options=options)
driver.get("https://staging.sso.strana.com/realms/strana/protocol/openid-connect/auth?client_id=partners&redirect_uri=https%3A%2F%2Fstagingpartner.strana.com%2Flk%2Ftrading&state=c2934501-50de-4617-9d2f-c72a1a0bb8fe&response_mode=fragment&response_type=code&scope=openid&nonce=79a31bf5-d356-44a3-8490-01a5acef06ed&code_challenge=ctmlHjsgOkgzWpD2mOLfhC1kQio4lwWpchH3AtTGCws&code_challenge_method=S256")
wait = WebDriverWait(driver, 20)

# === АВТОРИЗАЦИЯ ===
LOGIN_FIELD = ("xpath", "//input[@id='username']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//div[@id='kc-form-buttons']/button")

wait.until(EC.presence_of_element_located(LOGIN_FIELD)).send_keys("0000000070@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("tZq-WvH-NKp-x4B")
driver.find_element(*SUBMIT_BUTTON).send_keys(Keys.ENTER)
# time.sleep(1)

# === СОЗДАНИЕ ПРОЦЕДУРЫ ===
CREATE_PROC_BUTTON = ("xpath", "//button[contains(@class, 'button__primary') and contains(@class, 'kc-b-trading-list__create-btn')]")
SMR_PROC_BUTTON = ("xpath", "//button[.//span[text()='Процедура по СМР']]")

wait.until(EC.element_to_be_clickable(CREATE_PROC_BUTTON)).send_keys(Keys.ENTER)
# time.sleep(1)

wait.until(EC.element_to_be_clickable(SMR_PROC_BUTTON)).send_keys(Keys.ENTER)
# time.sleep(1)

# === НАИМЕНОВАНИЕ ===
NAME_FIELD = ("xpath", "//div[contains(@class, 'content-part')]//textarea")
wait.until(EC.presence_of_element_located(NAME_FIELD)).send_keys("1 автотест")
# time.sleep(1)

# === СКРОЛЛ К ДАТЕ ===
DATE_PLACEHOLDER = ("xpath", "//input[@placeholder='ДД.ММ.ГГ']")
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(*DATE_PLACEHOLDER))
# time.sleep(1)

# === КОММЕНТАРИЙ ===
COMMENT_EDITOR = ("css selector", ".ql-editor")
editor = driver.find_elements(*COMMENT_EDITOR)[0]
driver.execute_script("arguments[0].innerHTML = '<p>1 коммент</p>';", editor)
# time.sleep(2)

# === ВЫБОР ДАТЫ ОКОНЧАНИЯ ПОДАЧИ ЗАЯВОК ===
DATE_FIELD = ("xpath", "//input[@placeholder='ДД.ММ.ГГ']")
driver.find_elements(*DATE_FIELD)[1].click()
time.sleep(1)

day_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'react-calendar__tile') and .//abbr[text()='2']]")
for btn in day_buttons:
    if btn.get_attribute('disabled') is None:
        driver.execute_script("arguments[0].click();", btn)
        break
time.sleep(1)

# === ВЫБОР ВРЕМЕНИ ===
TIME_FIELD = ("xpath", "//input[@placeholder='ЧЧ.ММ']")
time_field = driver.find_elements(*TIME_FIELD)[1]
time_field.click()
time.sleep(1)
time_field.clear()
time_field.send_keys("21:00")
time_field.send_keys(Keys.ENTER)
time.sleep(1)

# === ВЫБОР СРОКОВ ПРОВЕДЕНИЯ РАБОТ ===
PERIOD_FIELD = ("xpath", "//input[@placeholder='ДД.ММ.ГГГГ – ДД.ММ.ГГГГ']")
driver.find_elements(*PERIOD_FIELD)[0].click()
time.sleep(1)

day_buttons_2 = driver.find_elements(By.XPATH, "//button[contains(@class, 'react-calendar__tile') and .//abbr[text()='2']]")
for btn in day_buttons_2:
    if btn.get_attribute('disabled') is None:
        driver.execute_script("arguments[0].click();", btn)
        break
time.sleep(1)

day_buttons_2 = driver.find_elements(By.XPATH, "//button[contains(@class, 'react-calendar__tile') and .//abbr[text()='2']]")
for btn in day_buttons_2:
    if btn.get_attribute('disabled') is None:
        driver.execute_script("arguments[0].click();", btn)
        break
time.sleep(1)

# === КНОПКА "СЛЕДУЮЩИЙ ШАГ" ===
NEXT_STEP_BUTTON = ("xpath", "//button[.//span[text()='Следующий шаг']]")
next_btn = wait.until(EC.presence_of_element_located(NEXT_STEP_BUTTON))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", next_btn)
time.sleep(4)



# ПЕРЕХОДИМ НА СТРАНИЦУ РДЦ

# Поле ввода (для клика, чтобы открыть список)
# === ПОИСК ПРАВИЛЬНОГО ДРОПДАУНА ===
print("🔍 Поиск поля 'Выберите проект'...")

# Находим все поля с placeholder "Выберите проект"
project_fields = driver.find_elements(By.XPATH, "//input[@placeholder='Выберите проект']")
print(f"Найдено полей: {len(project_fields)}")

for i, field in enumerate(project_fields):
    print(f"Поле {i}: видимо={field.is_displayed()}, доступно={field.is_enabled()}")

    # Кликаем по каждому полю и смотрим, что открывается
    field.click()
    time.sleep(2)

    # Проверяем, появился ли список с проектами
    options = driver.find_elements(By.XPATH, "//div[@data-floating-ui-wrap]//*")
    print(f"  Найдено вариантов: {len(options)}")

    for opt in options[:10]:  # Показываем первые 10
        if opt.text.strip():
            print(f"    {opt.text}")

    # Если нашли нужный вариант
    found = False
    for opt in options:
        if "Плеханово" in opt.text or "С. Плеханово" in opt.text:
            print(f"✅ Найден вариант: {opt.text}")
            opt.click()
            found = True
            break

    if found:
        break
    else:
        # Если не нашли, закрываем список (кликаем по полю ещё раз)
        field.click()
        time.sleep(1)

time.sleep(2)