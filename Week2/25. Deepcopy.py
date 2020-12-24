import copy

x = [1,2,[3,4]]
y = x.copy()
y[0], y[2][0] = 9,9
print(x)
	
z = copy.deepcopy(x)
print(z)

z[0],z[2][0] = 8,8
print(x)
print(z)