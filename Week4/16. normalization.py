from sklearn import datasets
from sklearn import preprocessing
import numpy as np
import pandas as pd

boston = datasets.load_boston()
# boston.data for data records
# boston.featurs_name for columns name
# boston.target for target attribute

# choose NOX, RM, AGE as sample datas

# boston.data[:,4:7] the first : if for axis0 
df = pd.DataFrame(boston.data[:,4:7])
df.columns = boston.feature_names[4:7]

# manual minmax method (df - df.min()) / (df.max() - df.min())
minmax = (df - df.min()) / (df.max() - df.min())

# minmax preprocessing from sklearn
preminmax = preprocessing.minmax_scale(df)

# manual z-score (df - df.mean()) / df.std()
z_score = (df - df.mean()) / df.std()

# z-score preprocessing
pre_z = preprocessing.scale(df)

# decimal scaling normalization
# manual
deci = df / 10 ** np.ceil(np.log10(df.abs().max()))