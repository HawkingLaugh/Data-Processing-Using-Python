import requests
import string

r = requests.get('https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.13676938943704742&callback=jQuery111203728483165332681_1608472316413&_=1608472316415')
#r.text = bunch of \u unicode strings.
for i in r.text:
    if i != string.ascii_lowercase and string.ascii_uppercase:
        print(r.text.encode('utf-8').decode('unicode-escape'),end=' ')      
        break
# print(r.text.encode('utf-8').decode('unicode-escape'))