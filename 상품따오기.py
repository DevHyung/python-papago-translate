import requests
from bs4 import BeautifulSoup
import json

f = open("titleList.txt",'w')
for pageIdx in range(1,3):
    url = 'https://www.thisiswhyimbroke.com/api/lists/new/{}?country=KR'.format(pageIdx)
    web = requests.get(url)
    jsonStr = json.loads(web.text)
    for post in jsonStr['posts']:
        print(post['title'])
        f.write(post['title']+'\n')
f.close()