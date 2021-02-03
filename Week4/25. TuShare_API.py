#%%
import tushare as ts
import numpy as np
import matplotlib.pyplot as plt

# stock = ts.get_hist_data('600848', start='2020-03-01', end='2020-03-10')
# print(stock)

# 1
stock = ts.get_hist_data('600036', start='2019-01-01', end='2019-03-31')
# df.iloc[:,0:end] to get data
stock_df = stock.iloc[:,0:5]
stock_df.sort_index(inplace=True)

# 2 print only high and low
print(stock_df.loc[:,['high', 'low']])

# 3 Output the date and the volume of the transaction with the lowest and the highest volume records in this quarter

sort_by_volume = stock_df.sort_values(by = 'volume')
min_day = sort_by_volume.iloc[0,:]
min_volume = min_day.volume
min_volume_date = min_day.name
print('The min volumne data is {}, the volume is {}'.format(min_volume_date, min_volume))

# 4 List the records with the volume above 100000
print(stock[stock.volume >= 100000])

# 5 Calculate the number of days in which the closing price (close) is higher than the opening price (open) in the first quarter the year

print(len(stock[stock.close > stock.open]))

''' 6 Calculate the rise and fall of the opening price two days before and after, 
the first output is to calculate the difference between every two days (the day after subtracting the previous day), 
and the second output is a list of the changing of opening price(the rise is indicated by 1 and the fall is indicated by -1)'''

print(stock.open.diff())
print(np.sign(np.diff(stock.open)))

# 7 Draw a line chart of the stock's highest and lowest price in January 2019
# stock.loc returns nothing??
# can't use raw stock data to loc, but can use the df after iloc
stock_new = stock_df.loc['2019-01-02':'2019-01-31',['high','low']]
stock_new.plot()

''' Plot the scatter chart between the difference between the daily closing price and 
opening price of the stock and the trading volume of the day in this quarter '''
plt.scatter(stock_df.close-stock_df.open, stock_df.volume)