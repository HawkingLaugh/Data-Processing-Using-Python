from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris.feature_names
iris_df['target'] = iris.target

# original target = 0,1,2 int32
print(iris_df.target)

# changing them by using DF.astype(type)
print(iris_df.target.astype(float))