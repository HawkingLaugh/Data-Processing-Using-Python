# %% for telling vscode to use notebook(Jupyter) for plot
#%%

import pandas as pd

quote = pd.read_csv('F:\GitHub\Data-Processing-Using-Python\MYM=F.csv', index_col='Datetime')
quote.fillna(quote.mean(), inplace = True)
quote.boxplot()
quote.loc['2021-01-22 02:19:20-05:00'] = [22032,34322,32442,12324.53]
# quote.iloc[:,0:4]
# 
# b = quote.boxplot()

# b = quote.describe()

# 3σ-principle based
c = quote[abs(quote - quote.mean()) > 3 * quote.std()]
quote[abs(quote - quote.mean()) > 3 * quote.std()].dropna(how='all')
