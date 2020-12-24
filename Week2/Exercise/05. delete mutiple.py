n = eval(input("Input number from 1~9: "))
count = 0
newStr = ''
for i in range(101):
    s = str(i)
    if i % n != 0:
        newStr = newStr + s + ','
        count += 1
        if count % 10 == 0:
            print(newStr[:-1])
            newStr = ''
if len(newStr) > 0:
    print(newStr[:-1])

# Another method
# Buggy
s = input()
i = int(s)
num = list(map(str, filter(lambda x : x % i and s not in str(x), range(1,101))))
for i in range(0, len(num), 10):
    print(','.join(num[i:i+10]))