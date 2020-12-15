i, j, k, l= 0, 0, 0, 0
count = 0
for i in range(3):
    for j in range(11):
        for k in range(21):
            l = 100 - 50 * i - 10 * j - 5 * k
            if l >= 0:
                count += 1

print('count = ', count)