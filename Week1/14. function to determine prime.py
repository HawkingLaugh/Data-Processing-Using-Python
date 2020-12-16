from math import sqrt
def isPrime(x):
    if x == 1:
        return False
    k = int(sqrt(x))
    #if hits any == 0, return False and continue. else, go to return True code
    for j in range(2, k+1):
        if x % j == 0:
            return False
    return True

for i in range(2, 101):
    #if isPrime return True, print that number
    if isPrime(i):
        print(i, end=' ')