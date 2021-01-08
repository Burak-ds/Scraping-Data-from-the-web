from selenium import webdriver
import pandas as pd
import time

browser = webdriver.Chrome('/Users/burakgun/Desktop/chromedriver')
url = 'https://eksisozluk.com/bos-yapmak--4364222?p='

pagecount = 1
entrylist = []
while pagecount <=9:
    new_url = url + str(pagecount)
    browser.get(new_url)
    elements = browser.find_elements_by_css_selector('.content')
    for element in elements:
        entrylist.append(element.text)
    pagecount +=1
frameim= pd.DataFrame({'Entryler' : entrylist}, columns=['Entryler'])
frameim.to_excel(r'entryler.xlsx', index = False)
browser.close()
