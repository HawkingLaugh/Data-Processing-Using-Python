#%%
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import scipy

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris.feature_names
iris_df['target'] = iris.target

# get the binning of the data
# returns 150 records in 3 bins, 50 each
iris_df.target.value_counts()
iris_df.target.value_counts().plot(kind = 'pie')
# %%
