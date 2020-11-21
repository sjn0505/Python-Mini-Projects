from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

pg=urlopen('https://www.espncricinfo.com/rankings/content/page/211271.html')
soup=BeautifulSoup(pg,'html.parser')

body=soup.find('div',{'class':'ciPhotoContainer'})

head=soup.findAll('h3')

name=[]
for i in head:
    j=i.text
    name.append(j)              #title of tables
#print(name[0])

columns=['pos','team','matches','points','rating']
df=pd.DataFrame(columns=columns)
print(df)

tr_list=soup.findAll('tr')

n=0
for i in tr_list:
    row=[]
    td_list=i.findAll('td')
    for j in td_list:
        a=j.text
        row.append(a)
    data={}
    try:
        for k in range(len(df.columns)):
            data[df.columns[k]] = row[k]
        df = df.append(data, ignore_index=True)
    except:
        df=pd.DataFrame(columns=columns)
        table_name=name[n]
        n=n+1
    df.to_csv('F:\\AIB\\Espncricinfo_'+table_name+'.csv', index=False)

print("done")
    