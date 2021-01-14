
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver
import time
from time import sleep
import pandas as pd

browser = webdriver.Chrome(r'C:\Users\haotr\Desktop\scrapy\chromedriver_win32\chromedriver')
browser.get('https://www.hrs-global.com/user-login')

username = browser.find_element_by_id('UserName')
username.send_keys('******************')

password=browser.find_element_by_id('Password')
password.send_keys('********')

browser.find_element_by_id('cmdSignIn').click()
time.sleep(1)
browser.get('https://www.hrs-global.com/order-tracking')

g = input('Enter Order ID to scrape:' )
order_number = browser.find_element_by_xpath("*//a[@title='"+g+"']")
order_number.click()

UPC=browser.find_elements_by_xpath("//small[contains(text(),'UPC Code')]")
Code=browser.find_elements_by_xpath("//small[contains(text(),'Code:')]")
QTY=browser.find_elements_by_xpath("//*[contains(@data-title, 'Qty ordered')]")
Price=browser.find_elements_by_xpath("//*[contains(@data-title, 'Price')]")
Picture=browser.find_elements_by_xpath("//td[contains(@class, 'order-review-content-picture')]/img")

Name_lst=[]
Name = browser.find_elements_by_xpath("//*[@class = 'order-review-content-description']//a")
for i in range(len(Name)):
    Name_lst.append(Name[i].get_attribute('title'))
    
UPC_lst=[]
for t in UPC:
    UPC_lst.append(t.text)
    
Code_lst=[]
for t in Code:
    Code_lst.append(t.text)

QTY_lst=[]
for t in QTY:
    QTY_lst.append(t.text)

Price_lst=[]
for t in Price:
    Price_lst.append(t.text)
    
Picture_lst = []
for t in Picture:
    Picture_lst.append(t.get_attribute("src"))

#Put above list of data into excel file with corresponding column's name   
df = pd.DataFrame({'Name': Name_lst,
                   'UPC': UPC_lst,
                   'Code': Code_lst,
                   'QTY': QTY_lst,
                   'Price':Price_lst,
                   'Picture':Picture_lst},columns=['Name','UPC', 'Code','QTY','Price','Picture'])

n = input('Save export csv file as:')
df.to_csv(n+'.csv', sep=',',index=False)

