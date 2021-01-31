from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn import preprocessing

boston = datasets.load_boston()
X = preprocessing.scale(boston.data)

pca = PCA(n_components='mle')
pca.fit(X)
print(pca.explained_variance_ratio_)