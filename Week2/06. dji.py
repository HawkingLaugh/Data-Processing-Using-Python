import requests
r = requests.get('https://money.cnn.com/data/markets/dow/')
status = r.status_code
if status == 200:
    print(r.text)