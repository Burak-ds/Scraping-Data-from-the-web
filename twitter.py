import pandas as pd
import numpy as np
import time
from termcolor import colored, cprint
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome('/Users/burakgun/Desktop/chromedriver')
url = 'https://twitter.com/'
browser.get(url)
ilk = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/a[2]/div/span")
ilk.click()
time.sleep(3)
kullanici = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
sifre = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")
kullanici.send_keys('ride_frankofon')
sifre.send_keys('Abdullah.1234')
login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span")
login.click()
time.sleep(1)

search = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
search.send_keys("#yazilimbilimi")
#JS SCROLL CODE'U
"""
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
        while(match==False):
                lastCount = lenOfPage
                time.sleep(3)
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                    match=True

"""
#JS SCROLL CODE'U
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(5)
tweetlistesi = []
for i in range(1,4):
    icerik = "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[{}]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div".format(i)
    tweets = browser.find_element_by_xpath(icerik)
    tweetlistesi.append(tweets.text)
browser.back()
browser.close()
frameim= pd.DataFrame({'Tweetler' : tweetlistesi}, columns=['Tweetler'])
frameim.to_excel(r'tweetler.xlsx', index = False)

