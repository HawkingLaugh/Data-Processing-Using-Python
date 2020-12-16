"""If a number is equal to the sum of its factors, 
the number is called the perfect number, for example, 6, because 6=1+2+3. 
Program and print all the perfect numbers within 1000."""

for i in range(1, 1001):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print('\n', i, " ", end="")
        print("it's factors are ", end="")
        for j in range(1,i):
            if i % j == 0:
                print(j, end = " ")