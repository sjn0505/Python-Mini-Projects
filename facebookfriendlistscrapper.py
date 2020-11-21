#pip install bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import time


browser=webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get('https://www.facebook.com/')

user_id='somemail@gmail.com'
password='password'

ep=browser.find_element_by_id("email")
ep.send_keys(user_id)

pw=browser.find_element_by_id("pass")
pw.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click() 

time.sleep(20)

profile=browser.find_element_by_xpath('//a[@class="_2s25 _606w"]')
profile.click()

time.sleep(4)

friends=browser.find_element_by_xpath('//ul[@class="_6_7 clearfix"]/li[3]/a')
friends.click()
time.sleep(0.2)

while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    browser.execute_script('window.scrollTo(0,0);')
    time.sleep(0.1)
    try:
        exit_control=browser.find_element_by_xpath("//*[contains(text(), 'More About You')]")
        break
    except:
        continue 

page_source=browser.page_source         #returning html file(source code) which browser is holding rn
soup=BeautifulSoup(page_source,'html.parser')

flist=soup.find('div',{'class':'_3i9'})

friend=[]
for i in flist.findAll('a'):
    friend.append(i.text)

names_list=[]
for name in friend:
    if(name=='FriendFriends'):
        continue
    if ('friends' in name):
        continue
    if(name==''):
        continue
    else:
        names_list.append(name)

print(names_list)
