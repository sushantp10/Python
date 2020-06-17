import requests
from bs4 import BeautifulSoup
import pprint
url="https://timesofindia.indiatimes.com/city/mumbai"
req=requests.get(url)
news=[]

if req.status_code==200:
    print("Successfully opened the web page")
    soup=BeautifulSoup(req.text,features="html5lib")
    list_news=soup.find("ul",{"class":"list5 clearfix"})
    for i in list_news.find_all("a"):
        news.append(i.text)
        #pprint.pprint(i.text)
else:
    print("Error")

#print("list news",news)
filename="Mumbai_News.txt"
with open(filename,"w+",newline='') as f:
    f.write("Mumbai Headlines \n\n")
    for item in news:
        f.write("%s\n"%item)
    f.close()
print("Mumbai Headlines successfully updated in file")
