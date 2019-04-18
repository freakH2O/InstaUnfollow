
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


def tryy(x):
    relay=True
    while relay==True:
        try:
            x.click()
            relay=False
        except Exception:
            continue

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument('user-data-dir= selenium')
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')

while True:
    browser.get('https://www.instagram.com')
    time.sleep(2)
    tryy(browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span'))
    time.sleep(2)
    tryy(browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a'))
    time.sleep(2)
    tryy(browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[1]/div/div[3]/button'))
    tryy(browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]'))
    time.sleep(random.randint(10,15))
