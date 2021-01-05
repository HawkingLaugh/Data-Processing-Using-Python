import numpy as np

# get determinant
x = np.array([[1,2],[3,4]])
r1 = np.linalg.det(x)
print(r1)

# Compute the (multiplicative) inverse of a matrix.
r2 = np.linalg.inv(x)
print(r2)

r3 = np.dot(x,x)
print(r3)