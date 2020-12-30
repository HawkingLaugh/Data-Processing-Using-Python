import requests
kw = {'q':'glenfiddich'}
r = requests.get('http://www.google.com/search', params=kw)
print(r.url)
# print(r.text)