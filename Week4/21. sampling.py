#%%
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris.feature_names

# for random sampling
# iris_df.sample()

iris_df['target'] = iris.target

# condition inside the []
iris_df[iris_df.target == 0]

# normal sampling after the stratifi
# combining two condition's results
A = iris_df[iris_df.target == 0].sample(frac=0.3)
B = iris_df[iris_df.target == 1].sample(frac=0.2)
A.append(B)
# %%
