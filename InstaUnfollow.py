import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument('user-data-dir= selenium')
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')


browser.get('https://www.instagram.com/accounts/login/')

#---------------------------------------------------------------------------------------------------------------------


def waituntilclickable(element,time):
    i=0
    while i<time:
        try:
            time.sleep(1)
            element.click()
            i=time
            i+=1
        except Exception:
            i+=1
            continue

#---------------------------------------------------------------------------------------------------------------------


relay=True
while relay==True:
   if browser.current_url == 'https://www.instagram.com/':
       browser.get('https://www.instagram.com/wear.horizon')
       break



try:
    login = browser.find_element_by_name('username')
    waituntilclickable(login,5)
    login.send_keys('wear.horizon', Keys.ENTER)
    password = browser.find_element_by_name('password')
    waituntilclickable(password, 5)
    password.send_keys('dcanoslimshady', Keys.ENTER)

    relay = True
    while relay == True:
        if browser.current_url == 'https://www.instagram.com/':
            browser.get('https://www.instagram.com/meme____machine___/')
            relay=False
except Exception:
    relay=True


#---------------------------------------------------------------------------------------------------------------------

relay=True

while relay==True:
    try:
      try:
        time.sleep(random.randint(3,10))
        following = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').click()
        time.sleep(2)
        browser.find_element_by_tag_name('html').send_keys(Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.SPACE)
        time.sleep(1)
        browser.find_element_by_tag_name('html').send_keys(Keys.TAB, Keys.SPACE)
        time.sleep(1)
        time.sleep(random.randint(3, 10))
        browser.refresh()
      except Exception:
          continue
    except Exception:
        continue

