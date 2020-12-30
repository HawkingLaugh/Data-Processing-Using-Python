import json
x = {"Name":"Hugo", "Address":{"Country":"Japan", "City":"Tokyo"}}
s_str = json.dumps(x)
print(s_str)
