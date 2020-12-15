from math import sqrt

j = 2
while j <= 100:
    i = 2
    k = sqrt(j)
    while i <= k:
        if j % i == 0: # j % i == 0 means there are factor inside == the number(j) not a prime number
            break
        i = i + 1
    if i > k:
        print(j, end=' ')
    j += 1