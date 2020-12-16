x = eval(input('x = '))
y = eval(input('y = '))
if x < y:
    x, y = y, x
while x % y != 0:
    r = x % y
    x = y
    y = r
print('result = ', y)