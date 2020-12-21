import re
import requests

def retrieve_dji_list():
    r = requests.get('https://money.cnn.com/data/markets/nasdaq/')
    
    # the first row, with each col's title
    # re.findall(regular expression pattern, string(requests.text also ok))
    head = re.findall('<thead>(.*?)</thead>', r.text)
    assert len(head)==1
    table_head = ['Company'] + re.findall('<th>(.+?)<', head[0])
    
    # pattern to get info of each company
    tbody_pat = re.compile('tbody>(.*?)</tbody')
    # tbody = the whole content inside teh tbody tag. return all contents as a 1 length List 
    tbody = re.findall(tbody_pat, r.text)
    assert len(tbody) == 1
    
    # to get all items that match the pattern in the list - tbody
    tr_pat = re.compile('<tr>(.*?)</tr>')
    tr_list = re.findall(tr_pat, tbody[0])
    print(tr_list)

    # table_pat to erase all html tag and get only those data between those tags
    table_pat = re.compile('>([^<^&]+?)<')
    stock_list = [table_head]
    for i in tr_list:
        s = re.findall(table_pat, i)
        stock_list.append(s)
    return stock_list

dji_list = retrieve_dji_list()
for i in dji_list:
    print(i)