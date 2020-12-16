i, j, k, l, m, n = 0, 0, 0, 0, 0, 0
count = 0
for i in range(3):
    for j in range(11):
        for k in range(21):
            for l in range(101):
                for m in range(201):
                    n = 1000 - 500 * i - 100 * j - 50 * k - 10 * l - 5 * m
                    if n >= 0:
                        count += 1

print('count = ', count)