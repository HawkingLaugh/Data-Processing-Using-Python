from math import sqrt

for i in range(2,101):
    flag = 1
    k = int(sqrt(i))
    for j in range(2, k+1):
        # if not prime, use flag = 0 and break the inside for loop, then go to the next if condition
        if i % j == 0:
            flag = 0
            break
    if flag:
        print(i, end=' ')