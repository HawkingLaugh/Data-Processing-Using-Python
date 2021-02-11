#%%
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
# import scipy

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris.feature_names
iris_df['target'] = iris.target

iris_df.iloc[:,0].mean()
iris_df.iloc[:,0].median()
iris_df.iloc[:,0].std()

# default argument = 0.5 = median
iris_df.iloc[:,0].quantile()

# get the upper and lower quad
# returns a Series
iris_df.iloc[:,0].quantile([0.25,0.75])

# extract the result of .quantile([0.25,0.75]) to calculate the interquartile range
iris_df.iloc[:,0].quantile([0.75]).loc[0.75] - iris_df.iloc[:,0].quantile([0.25]).loc[0.25] 

# cal from .describe()
iris_df.iloc[:,0].describe().loc['75%'] - iris_df.iloc[:,0].describe().loc['25%']


# %%
