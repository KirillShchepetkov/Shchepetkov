import json
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://staging.sso.strana.com/realms/strana/protocol/openid-connect/auth?client_id=partners&redirect_uri=https%3A%2F%2Fstagingpartner.strana.com%2Flk%2Ftrading&state=c2c6de16-83ef-4f2d-849a-a6668506a1dc&response_mode=fragment&response_type=code&scope=openid&nonce=b3f05b31-faff-4d14-ba8c-f1a7e652381e&code_challenge=4TIkmuTii1ex6q3mJW-86Wz2alwEdsaX_GvhZKaNMt8&code_challenge_method=S256")

input()

cookies = driver.get_cookies()
with open('cookies.json', 'w') as file:
    json.dump(cookies, file, indent=4)

    # Получение куки










