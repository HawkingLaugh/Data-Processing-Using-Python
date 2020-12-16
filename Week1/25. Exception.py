# try:
#     num1 = int(input('input number 1: '))
#     num2 = int(input('input number 2: '))
#     print(num1 / num2)
# except ZeroDivisionError as err:
#     print('Number 2 cannot be Zero')
# except ValueError as e:
#     print('Please input a digit')

while True:
    try:
        num1 = int(input('input number 1: '))
        num2 = int(input('input number 2: '))
        print(num1 / num2)
    except (ZeroDivisionError, ValueError) as err:
        print('invalid input')
    else:
        print('Aha, all OK')