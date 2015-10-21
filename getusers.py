import requests
import time
import re
import random
def users(Mlink):
    userlist = []
    i = 0 #count how many page can get until get denied
    inside = Mlink+'reviews?start=0&filter='
    try:
        while 1:
            page = getpage(inside)
            namelinks = re.findall(r'http://www\.douban\.com/people/.*?/',page)
            nextlink = re.findall(r'start.*?next',page)
            if len(nextlink) != 0:
                start = re.findall(r'\d+',nextlink[0])
                inside = Mlink+'reviews?start='+str(start[0])+'&filter=&limit=20'
                userlist.extend(namelinks)
                i = +1
                time.sleep(random.uniform(0,2))
            else :
                break
    except:
        f.open('breakpoint.txt','w')
        f.write(Mlink+'\n')
    return userlist

def getpage(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
               'host':'movie.douban.com',
               'reference':'http://www.douban.com/'
               }
    page = requests.get(url,headers=headers).content.decode('utf-8','ignore')
    return page

def reselect(former):
    total = len(former)
    after = []
    for j in range(0,total):
        if j%2 ==0:
            after.append(j)
    return after
