import requests
from bs4 import BeautifulSoup
import re

s = 0
r = requests.get('https://book.douban.com/subject/1084336/')
soup = BeautifulSoup(r.text, 'lxml')
pt = soup.find_all('span', {'class':'short'})
for i in pt:
    print(i.string)

ps = re.compile('<span class="user-stars allstar40 rating" title="推荐"></span>')
#refind returns a list
refind = re.findall(ps, r.text)
for star in refind:
    s += int(star)
print(s)