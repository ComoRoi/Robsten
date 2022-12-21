from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import config
import telegram
import datetime
import requests

# 설정값 관리
comConSet = config.COMMON_CONFIG
tele_token = comConSet['tele_token']
chat_id = comConSet['chat_id']
bot = telegram.Bot(token=tele_token)
now = datetime.datetime.now()
nowDatetime = now.strftime('[%Y-%m-%d %H:%M:%S] ')
targetService = '[WEB Service] '
getTokenUrl = 'https://faucet.egorfine.com/'
tokenAddress = comConSet['rcvWalletAddress']
exeDir = comConSet['exeDir']

# Window 옵션 생성
chrome_options = webdriver.ChromeOptions()

# Window 창 숨기는 옵션 추가
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--incognito')  # Option 기능 테스트를 위해 임시로 코드 추가

chrome_path='/opt/Webdriver/chromedriver'
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)

def currentTime():
    global nowDatetime
    nowDatetime = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')
    return nowDatetime

def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 ⌘F8을(를) 누릅니다.


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    # print_hi('PyCharm')

    try :
        response = driver.get(url=getTokenUrl)

    except:
        bot.sendMessage(chat_id=chat_id, text='Selenium can not open the web.')
        print(currentTime() + targetService + 'Selenium can not open the web.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "address"))).send_keys(tokenAddress)
        #driver.find_element((By.ID,"address")).send_keys(tokenAddress)
        #driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/div/form/button').click()
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[1]/div/form/button'))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div/form/div/input'))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div/form/button'))).click()

        deltatime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div/div/b[2]'))).text
        print(currentTime() +"Will be retry in "+deltatime)
        ### https: // www.daleseo.com / python - time /

        bot.sendMessage(chat_id=chat_id, text=deltatime + 'Robsten wallet receive complete.')

    except:
        #bot.sendMessage(chat_id=chat_id, text='Can not send ethereum for testnet.')
        print(currentTime() + targetService + 'Can not send ethereum for testnet.')

time.sleep(5)
driver.quit()



