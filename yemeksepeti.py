import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browse = webdriver.Chrome("/Users/burakgun/Desktop/chromedriver")
url = "https://www.yemeksepeti.com/"
browse.get(url)
time.sleep(1)
istanbul = browse.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div/a[30]/div/span")
istanbul.click()
time.sleep(10)
try:
    search = browse.find_element_by_css_selector("input.select2-search__field")
except:
    search = browse.find_element_by_xpath("//*[@id='ys-areaSelector-droparea']/span/span/span[1]/input")
search.send_keys("Tüm Semtler")
search.send_keys(Keys.RETURN)
buton = browse.find_element_by_xpath("/html/body/header/div/div/div/div[4]/button")
buton.click()
time.sleep(3)
ordering = browse.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div/button[3]")
ordering.click()
time.sleep(3)
"""lenOfPage = browse.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browse.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True"""
restaurantlar = browse.find_elements_by_css_selector("div.head")
restaurant_isimleri = browse.find_elements_by_css_selector("a.restaurantName")
restaurantsss = []
restaurant_liste =[]
for isims in restaurant_isimleri:
    restaurantsss.append(isims.text)
for restaurant in restaurantlar:
    restaurant_liste.append(restaurant.text)



puanlar = []
for yer in restaurant_liste:
    puanlar.append(yer.split("\n")[0])
df = pd.DataFrame({'Restaurants' : restaurantsss,'Puanlar' : puanlar}, columns=['Restaurants','Puanlar'])
df.to_excel(r"lokantalar.xlsx",index=False)

browse.close()
