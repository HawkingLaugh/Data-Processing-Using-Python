def f(x = True):
    'whether x is a correct word or not'
    if x:
        print('x is a correct word')
    print('OK')

f()
f(False)

def g(x, y = True):
    "x and y both correct words or not"
    if y:
        print(x, 'and y both correct')
    print(x,'is OK')
g(68)
g(68, False)