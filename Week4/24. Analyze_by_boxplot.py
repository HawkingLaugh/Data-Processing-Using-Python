#%%
import pandas as pd
# pd.read_excel() returns a pd DF
score = pd.read_excel('F:\GitHub\Data-Processing-Using-Python\score.xlsx')
score.boxplot()
# %%
