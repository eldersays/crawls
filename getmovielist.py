import requests
import time
import re


def geturl(url):
    page = requests.get(url).content.decode('utf-8')
    return page
def getlist(Rpage):
    list = re.findall(r'http://movie\.douban\.com/subject/.*?/',Rpage)
    return list
a = 0
for i in range(0,225,25):
    try:
        Dpage = geturl('http://movie.douban.com/top250?start='+str(i)+'&filter=&type=')
        lists = getlist(Dpage)
        f =open('urls.txt','a')
        for i in lists:
            f.write(i+'\n')
    except:
        f.write(a)
        break
