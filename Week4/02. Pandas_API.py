import pandas_datareader.data as web
f = web.DataReader('AXP', 'stooq')
print(f.head(5))

# supported data source
'''
Tiingo
IEX
Alpha Vantage
Enigma
Quandl
St.Louis FED (FRED)
Kenneth French’s data library
World Bank
OECD
Eurostat
Thrift Savings Plan
Nasdaq Trader symbol definitions
Stooq
MOEX
Naver Finance
'''