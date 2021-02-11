from sklearn import datasets, svm

clf = svm.SVC(gamma=0.001, C=100.)
digits = datasets.load_digits()

# clf.fit(training vector, target value)
clf.fit(digits.data[:-1], digits.target[:-1])
result = clf.predict(digits.data)
print(result)