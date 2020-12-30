import json
with open('example_1.json', 'r+') as f:
    data = json.load(f)
print(data)

with open('example_2.json', 'r+') as f:
    data2 = json.load(f)
print(type(data2))