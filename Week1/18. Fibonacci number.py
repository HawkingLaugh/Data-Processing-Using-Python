import time
start_time = time.time()
#the nth Fibonacchi number
def fib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    print(a)

fib(32)
print('{} seconds'.format(time.time() - start_time))