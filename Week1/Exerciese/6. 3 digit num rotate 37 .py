"""If a three-digit integer is a multiple of 37, 
then the two other rotated three-digit numbers of the number are also a multiples of 37 (for example, 123 to 231 and 312)."""

for num in range(100,1000):
    # example 148
    if num % 37 == 0:
        tempNum1 = num % 100 * 10 + num // 100 # 148 % 100 = 48 * 10 + 148 // 100 = 1 = 481
        tempNum2 = num % 10 * 100 + num // 10 # 148 % 10 = 8 * 100 + 148 // 10 = 14 = 841
        if tempNum1 % 37 != 0 or tempNum2 % 37 != 0:
            print("It's False")
            break
else:
    print('True')