import requests, bs4
import time
import os
from os.path import join

print(os.getcwd())
##making the dir where all the files going to store

if not (os.path.exists(os.path.join(os.getcwd(),"xkcd"))):
    os.mkdir("xkcd")

for i in range(2067,2065,-1):
    res=requests.get('https://xkcd.com/'+str(i)+'/')
    Soup = bs4.BeautifulSoup(res.text, 'html.parser')

    images=Soup.find_all('img')[2]
   
    filename="http:"+images.get("src")
    print(filename)
    print(os.getcwd())
    dirp=r'C:\Users\lenovo\MypythonScripts'
    
    
    try:
        page=requests.get(filename)
        path=dirp+r"\xkcd\newfile"+str(i)+".jpg"
        print(path)
        with open(path,'wb') as p:
            p.write(page.content)
    except:
        pass



##src="/2067/asset/challengers_header.png"
##src="//imgs.xkcd.com/comics/election_night.png"

##http://imgs.xkcd.com/comics/recurring_nightmare.png
