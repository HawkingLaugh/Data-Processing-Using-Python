import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.masterofmalt.com/whiskies/glenmorangie/glenmorangie-a-tale-of-cake-whisky/')
soup = BeautifulSoup(r.text, 'lxml')
# pattern = soup.find_all('div', {'id':'whiskyDetailsWrapper'})
a = soup.find_all('span', {'class':'kv-val'})
for i in a:
    if i.string != "Info not yet available":
        print(i.string)

bottleName = ''
temp_url = 'https://www.masterofmalt.com/whiskies/glenmorangie/{}'.format(bottleName)