from sklearn import datasets
import pandas as pd

boston = datasets.load_boston()

df = pd.DataFrame(boston.data[:,4:7])
df.columns = boston.feature_names[4:7]

pd.cut(df.AGE, 5, labels = range(5))
pd.qcut(df.AGE, 5, labels = range(5))
# set data range by adding slice[:] into the first arugment

print(pd.qcut(df.AGE[:20], 5, labels = range(5)))

