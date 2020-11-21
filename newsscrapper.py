from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

p=int(input("Enter number of pages: "))

titles=[]
links=[]
for i in range(p):
    url="https://news.ycombinator.com?p="+str(i+1)
    r=urllib.request.urlopen(url)
    c=r.read()
    soup=BeautifulSoup(c,'html.parser')
    d=soup.find('table',{'class':'itemlist'}).find_all('a',{'class':'storylink'})

    for j in d:
        title=j.text
        titles.append(title)
        link=j.get('href')
        links.append(link)

dic={'news_title':titles,'url':links}
df=pd.DataFrame(dic)

df.to_csv("F:\\AIB\\News.csv", index=False)
print("Done")
