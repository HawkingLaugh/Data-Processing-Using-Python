global_str = 'hello'
def foo():
    local_str = 'world'
    return global_str + local_str

a = 3
def f():
    a = 5
    print(a ** 2)
#Result = 25

def g(x):
    global a
    print(a)
    a = 5
    print(a + x)

print(a)
a = 3
g(8)
print(a)