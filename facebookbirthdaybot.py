#download selenium using pip install
#Since I used Chrome. download Chromedriver of your Chrome version from online
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument("--disable-notifications")


browser=webdriver.Chrome('C:\chromedriver\chromedriver.exe') #to open chrome browser. ps: its loction where i kept the chromedriver.exe
browser.get('https://www.facebook.com/')                     #to open the required link in the browser

#user_id=input("Enter email or phone number:")
#password=input("Enter password:")

user_id= "mail@gmail.com"
password="password"

ep=browser.find_element_by_id("email")                      #to find the input field using id
ep.send_keys(user_id)                                       # to send a value to that input

pw=browser.find_element_by_id("pass")
pw.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()                                               #to click on the button

#browser.switch_to_alert().dismiss()
#browser.quit()                                             #to close browser

time.sleep(20)

'''
k= '//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
#k= '//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
n=browser.find_element_by_xpath(k).get_attribute('textContent')
'''

'''
num=n[0]
num=int(num)
print(num)
'''
#for my program
#num=1

#message= "Happy Birthday!"
browser.get('https://www.facebook.com/events/birthdays/')


#bday_list = browser.find_elements_by_xpath("//*[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")

#c=0
'''
for element in bday_list:
    element_id= str(element.get_attribute('id'))
    XPATH='//*[@id=" ' + element_id + ' "]'
    post=browser.find_element_by_xpath(XPATH)
    post.send_keys(message)
    #time.sleep(1)
    post.send_keys(Keys.RETURN)
    c=c+1
    if(c>num):
        break
'''

#browser.quit()



k='//*[@id="birthdays_content"]/div[1]'
tBirthday=browser.find_element_by_xpath(k)                      #Finds today's birthdays

container_list=tBirthday.find_elements_by_tag_name('textarea')  #Finds all of the textareas under today's birthdays only

#Iterates through all the text areas collected on previous step

for container in container_list:                                   

    container.send_keys("Happy Birthday :)")                    #Input Message into Box    

    container.send_keys(Keys.ENTER)                             #Presses ENTER Key

#browser.quit()