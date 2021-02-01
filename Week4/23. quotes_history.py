import requests
import re
import json
import pandas as pd
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'http://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)  
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])     # m = ['[{...},{...},...]']
        quotes = quotes[::-1]
    return  [item for item in quotes if 'type' not in item]
 
quotes = retrieve_quotes_historical('AXP')
quotesdf_ori = pd.DataFrame(quotes)
quotesdf = quotesdf_ori.drop(['adjclose'], axis = 1)
print(quotesdf)