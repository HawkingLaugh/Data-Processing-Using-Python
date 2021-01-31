import pandas as pd

quote = pd.read_csv('MYM=F.csv', index_col='Datetime')
quote.fillna()
print(quote)