from sklearn import datasets
from sklearn import preprocessing

boston = datasets.load_boston()
X = boston.target.reshape(-1,1)

Y = preprocessing.Binarizer(threshold= 20.0).fit_transform(X)
print(Y)
