
# coding: utf-8

# In[ ]:


import selenium
from selenium import webdriver
import time
from time import sleep
import pandas as pd

browser = webdriver.Chrome(r'C:\Users\haotr\Desktop\scrapy\chromedriver_win32\chromedriver')
browser.get('https://uniqueindustries.handshake.com/account/login')

username = browser.find_element_by_id('id_username')
username.send_keys('*********************')

password=browser.find_element_by_id('id_password')
password.send_keys('***********')

browser.find_element_by_xpath("//*[contains(@value, 'Log in')]").click()  
time.sleep(1)
browser.get('https://uniqueindustries.handshake.com/b/orders')

g = input('Enter Order ID to scrape:' )
browser.get('https://uniqueindustries.handshake.com/b/orders/'+g)

sec = input('Let us wait for user input. Let me know how many seconds to sleep now.\n')
time.sleep(int(sec))

details = browser.find_elements_by_xpath("//*[contains(@class,'icon-info-sign')]")

UPC_lst=[]
Name_lst=[]
SKU_lst=[]
Price_lst=[]
QTY_lst =[]
Picture_lst=[]

for i in range(len(details)):
 
    details[i].click()
    
    sleep(1)
    
    print(i)
    UPC_popup=browser.find_elements_by_xpath("//*[@id='order']/div[4]/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[3]/td[2]")[0].text
    UPC_lst.append(UPC_popup)
    
    
    Name_popup=browser.find_elements_by_xpath("//*[@id='order']/div[4]/div/div[2]/div[1]/div[2]/div[2]/h3")[0].text
    Name_lst.append(Name_popup)
    
    SKU_popup=browser.find_elements_by_xpath("//*[@id='order']/div[4]/div/div[2]/div[1]/div[2]/div[2]/p[1]/span[2]")[0].text
    SKU_lst.append(SKU_popup)
    
    Price_popup = browser.find_elements_by_xpath("//*[@id='order']/div[4]/div/div[2]/div[1]/div[2]/div[2]/p[1]/span[1]/span")[0].text
    Price_lst.append(Price_popup)
    
    QTY_popup=browser.find_element_by_name("qty").get_attribute('value')
    QTY_lst.append(QTY_popup)
    
    Picture_popup =  browser.find_elements_by_xpath("//*[@id='order']/div[4]/div/div[2]/div[1]/div[1]/a/span/img")[0].get_attribute('src')
    Picture_lst.append(Picture_popup)
    
    browser.find_elements_by_xpath("//*[@class = 'icon-remove']")[0].click()
    sleep(0.3)

df = pd.DataFrame({'UPC': UPC_lst,
                   'Name': Name_lst,
                   'SKU': SKU_lst,
                   'QTY': QTY_lst,
                   'Price':Price_lst,
                   'Picture':Picture_lst},columns=['Name','UPC', 'SKU','QTY','Price','Picture'])

n = input('Save export csv file as:')
df.to_csv(n+'.csv', sep=',',index=False)

