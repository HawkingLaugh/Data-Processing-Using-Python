import numpy as np
aArray = np.array([1,2,3])
print(aArray)
bArray = np.array([(1,2,3),(4,5,6)])
print(bArray)
# np.arange(start, stop, step)
c = np.arange(1,5,0.5)
print(c)
# return random floats between 0,1.0
d = np.random.random((2,2))
print(d)
# np.linspace(start, stop, nums, )
e = np.linspace(1,2,10,endpoint=False)
print(e)

# np.ones(shape, dtype=, order='') an ndarray with axis 0 = 2, axis 1 = 3 filled with one
f = np.ones([2,3])
print(f)

# np.zeros(shape, dtype=, order='') an ndarray with axis 0 = 2, axis 1 = 2, filled with zeros
g = np.zeros((2,2))
print(g)

# np.fromfunction(function, shape, dtype=, order='') an ndarray with function:(lambda i,j:(i+1)*(j+1)) and shape(9,9)
h = np.fromfunction(lambda i,j:(i+1)*(j+1),(9,9))
print(h)

# creating a 4x4 ndarray with filled with 1-16(1,17)
i = np.arange(1,17).reshape(4,4)
print(i)

j = np.array([1,3,7])
k = np.array([3,5,8])
print(np.vstack((j,k)))
print(np.hstack((j,k)))

l = np.array([(5,5,5),(5,5,5)])
m = np.array([(2,2,2),(2,2,2)])
print(l*m)
print(l+m)

n = np.array([1,2,3])
o = np.array([[1,2,3],[4,5,6]])
print(n+o)

