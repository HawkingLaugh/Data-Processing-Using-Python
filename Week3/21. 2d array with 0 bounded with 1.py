import numpy as np

x = np.ones((10,10))
x[1:-1,1:-1] = 0

y = np.full((10,10),1)

X = np.array([[1,2,3],[4,5,6]], dtype=np.float64)

#unit array

np.identity(10)
np.eye(5, k = -2)

np.random.normal(0,5,100)
a = np.random.uniform(-5,5,100)

# random sample from 2d array
b = np.random.rand(3,5)
mask = np.random.choice(np.arange(b.shape[0]), 2, replace=True)

# replace data inside array and np.where()
c = np.arange(1,101)
c[c<=50]
c[(c>50) & (c % 2 == 0)]
# c[c % 2 == 0] = -1
d = np.where(c % 2 == 0, -1 , c)

# Boardcasting

scores = np.array([[98,76,87], [76,88,91]])
score_mean = scores.mean(axis = 1, keepdims=True)
print(scores - score_mean)
