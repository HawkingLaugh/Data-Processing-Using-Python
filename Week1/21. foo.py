def foo(num,base):
    if num >= base:
        foo(num // base, base)
    print(num%base, end = ' ')

# numA = int(input())
# numB = int(input())

numA = 126
numB = 2
foo(numA, numB)