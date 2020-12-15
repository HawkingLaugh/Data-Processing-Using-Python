def f1(a, b):
    '模擬加法實現乘法的過程'
    if b == 1:
        return a
    else:
    # need return to return the result that not yet a real value
        return a + f1(a, b - 1)

def f2(n):
    'convert dec to bin'
    if n >= 2:
        f2(n // 2)
    print(n % 2, end=' ')