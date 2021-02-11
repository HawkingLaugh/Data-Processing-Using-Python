#%%
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris.feature_names
iris_df['target'] = iris.target
X = [item[0] for item in iris.data]
Y = [item[2] for item in iris.data]

# cal the correlation coefficient between 0 1 4 attributes of iris
iris_df.iloc[:,[0,1,4]].corr()

# cal the correlation coefficient between 2 attributes of iris
iris_df['target'].corr(iris_df.iloc[:,0])

# heatmap from seaborn to observe correlation coefficient between 0 1 4 attributes
sns.heatmap(iris_df.iloc[:,[0,1,4]].corr(), annot=True, fmt='.1f', cmap='rainbow')
# %%
