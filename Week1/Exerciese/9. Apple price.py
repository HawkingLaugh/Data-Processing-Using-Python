while True:
    try:
        count = int(input('Enter count: '))
        price = float(input('Enter price for each one: '))
        total = count * price
        print('The price is {}'.format(total))
        break
    except ValueError as e:
        print('Error, please enter numeric one.')