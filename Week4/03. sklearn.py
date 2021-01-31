from sklearn import datasets

iris = datasets.load_iris()
print(iris.data)
print(iris.feature_names)
print(iris.data.shape)
print(iris.target)