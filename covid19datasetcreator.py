from selenium import webdriver
import pandas as pd
import time
import os

browser=webdriver.Chrome('C:\chromedriver\chromedriver.exe')
time.sleep(0.2)
browser.get('https://www.worldometers.info/coronavirus/')
time.sleep(20)


df=pd.DataFrame(columns=['Rank','Country','Total Cases','New Cases','Deaths','New Deaths','Recovered','Active cases','Critical'])


for i in browser.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr') :
    td_list=i.find_elements_by_tag_name('td')
    row=[]
    for td in td_list:
        row.append(td.text)
    
    data={}
    
    for j in range(len(df.columns)):
        data[df.columns[j]]=row[j] 
    df=df.append(data, ignore_index=True)

df=df[1:]
path='F:\\AIB'
path1=os.path.join(path,'covid.csv')
df.to_csv(path1, index=False)

print("The data is stored at: "+path1+".")
print(df)




time.sleep(0.3)
browser.quit()
