import requests
import re
import pandas as pd
 
def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/markets/nasdaq/')
     
    head = re.findall('<thead>(.*?)</thead>', r.text)
    # assert condition. if condition == True, nothing happen. if False, raise error(insert error by using : and treat it like normal try if)
    # only run the following when head is single list
    assert len(head)==1
    table_head = ['Company'] + re.findall('<th>(.+?)<', head[0])
   
    tbody_pat = re.compile('tbody>(.*?)</tbody')
    tbody = re.findall(tbody_pat, r.text)
    assert len(tbody) == 1
     
    tr_pat = re.compile('<tr>(.*?)</tr>')
    tr_list = re.findall(tr_pat, tbody[0])
     
    table_pat = re.compile('>([^<^&]+?)<')
    stock_list = [table_head]
    for i in tr_list:
        s = re.findall(table_pat, i)
        stock_list.append(s)
    return stock_list
 
dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list)
print(djidf)