import requests
r = requests.get('https://www.masterofmalt.com/whiskies/glenmorangie/glenmorangie-a-tale-of-cake-whisky/')

print(r.status_code)
print(r.text)