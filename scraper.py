from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import credentials
#利用options模組設定關閉通知設定
option = Options()
option.add_argument("--disable-notifications")

driver= webdriver.Chrome(options=option)

driver.get("https://www.facebook.com/")
##定位帳號及密碼位置
email = driver.find_element(By.ID,"email")
password = driver.find_element(By.ID,"pass")
#利用credential存取帳號及密碼
email.send_keys(credentials.email)
password.send_keys(credentials.password)
password.submit() #在密碼位置送出

time.sleep(10)
