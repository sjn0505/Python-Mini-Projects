from selenium import webdriver
import urllib.request

user_h=input("Enter the user name whose profile pic you want: ")
browser=webdriver.Chrome('C:\chromedriver\chromedriver.exe')


url='https://www.instagram.com/'
url_p=url+user_h

browser.get(url_p)

try:
    img=browser.find_element_by_xpath('//img[@class="_6q-tv"]')

except:
    img=browser.find_element_by_xpath('//img[@class="be6sR"]')

img_link=img.get_attribute('src')

path = "F:\\"+user_h+".jpg"

urllib.request.urlretrieve(img_link,path)
print("Profile pic downloaded at: "+path)

browser.quit()