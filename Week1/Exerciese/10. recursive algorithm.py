def proc(n):
    if n < 0:
        print('-', end='')
        n = -n
    if n // 10:
        proc(n // 10)
    print(n % 10, end='')
proc(-345)

"""
-345 345
proc(345) 345 // 10 = 34
proc(34)  34  // 10 = 3
proc(3)   3  //  10 = 0

proc(3)   3   %   10 = 3
proc(34)  34  %   10 = 4
proc(345) 345 %   10 = 5

print result
-345
"""