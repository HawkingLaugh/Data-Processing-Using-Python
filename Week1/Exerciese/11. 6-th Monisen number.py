""" Classic Programming Question: 
find the n-th Monisen number. 
A number M is a Monisen number if M=2**P-1 and both M and P are prime numbers. 
For example, if P=5, M=2**P-1=31, 5 and 31 are both prime numbers, so 31 is a Monisen number. """

import math

pList = []
mList = []
def prime(x):
    if x == 1:
        return False
    n = int(math.sqrt(x))
    for i in range(2, n+1):
        if x % i == 0:
            return False
    return True

def generateM():
    for i in pList:
        M = (2 ** i) - 1
        if prime(M):
            mList.append(M)
            print(mList)
        else:
            continue

for i in range(1000):
    if prime(i):
        pList.append(i)
        print(pList)
generateM()
print(mList)