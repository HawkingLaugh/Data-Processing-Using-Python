#i, j, k as digits and range of number(1,2,3,4)
'''solve how many non-repetitive three-digit numbers can be composed of these four numbers of 1-4, and output these numbers in ascending order.'''
# range starts from 1 there for result in ascending order
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                print(100*i+10*j+k)