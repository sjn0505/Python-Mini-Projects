#download selenium using pip install
#Since I used Chrome. download Chromedriver of your Chrome version from online
from selenium import webdriver


browser=webdriver.Chrome('C:\chromedriver\chromedriver.exe') #to open chrome browser. ps: its loction where i kept the chromedriver.exe
browser.get('https://www.facebook.com/')                     #to open the required link in the browser

#user_id=input("Enter email or phone number:")
#password=input("Enter password:")

user_id= "yourmailid@gmail.com"
password="yourpassword"

ep=browser.find_element_by_id("email")                      #to find the input field using id
ep.send_keys(user_id)                                       # to send a value to that input

pw=browser.find_element_by_id("pass")
pw.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()                                               #to click on the button

#browser.quit()                                             #to close browser
