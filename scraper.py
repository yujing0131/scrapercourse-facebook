from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import credentials
from bs4 import BeautifulSoup
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

time.sleep(5)

driver.get('https://www.facebook.com/ETtodayMOVIE')
#設定滑鼠滾輪的次數
for i in range(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

soup = BeautifulSoup(driver.page_source,'lxml')

result=[]
posts = soup.find_all("div" ,{"class":"x1iorvi4 x1pi30zi x1l90r2v x1swvt13"})
# print(posts)
for post in posts:
    content = post.find(
        "span",{"class":"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"})
    result.append(content.getText())

print(result)