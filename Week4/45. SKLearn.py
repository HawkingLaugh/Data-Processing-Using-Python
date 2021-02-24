#%%
from sklearn import datasets, neighbors, cluster, svm

iris = datasets.load_iris()
# all data inside the dataset
iris.data

# the shape of data
iris.data.shape

# the target value of the dataset 
iris.target


# KNN
knn = neighbors.KNeighborsClassifier()
# knn.fit(training data, target data)
knn.fit(iris.data, iris.target)
# predict
knn.predict([[5.0, 3.0, 5.0, 2.0]])


# k-means clustering algorithm
kmeans = cluster.KMeans(n_clusters=3).fit(iris.data)

# Determine the data types
pred = kmeans.predict(iris.data)

# print out the label of each data entry that has benn predicted
for label in pred:
    print(label, end = ' ')
print('\n')
# print out the correct labels that are originally marked
for label in iris.target:
    print(label, end = ' ')


# SVM
svc = svm.LinearSVC()
svc.fit(iris.data, iris.target) # learn phase
svc.predict([[5.0, 3.0, 5.0, 2.0]])
# %%
