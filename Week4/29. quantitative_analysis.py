#%%
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import scipy

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris.feature_names
iris_df['target'] = iris.target

plt.hist(iris_df.iloc[:,0], 30, color='c')
scipy.stats.normaltest(iris_df.iloc[:,0], axis=0)
# %%
