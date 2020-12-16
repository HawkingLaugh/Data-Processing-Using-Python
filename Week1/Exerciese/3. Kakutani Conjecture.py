'''for a positive integer n, 
divide by 2 for even numbers, 
multiply by 3 plus 1 for odd numbers, and get a new one. 
Continue to calculate according to the previous two rules, the result obtained after several times must be 1.
if odd number, * 3 + 1 to become a even number, then do the 2 dividen again
'''

n = int(input('input a positive interger: '))

while n != 1:
    if n % 2 == 0:
        print("{} / 2 = {}".format(n, n//2))
        n //= 2
    else:
        print("{} * 3 + 1 = {}".format(n, n*3+1))
        n = 3*n+1