from random import randint

x = randint(0,300)

while True:
    y = int(input('tell me your guess between 0~300: '))
    if x > y:
        print('too small, guess higher')
        continue
    elif x < y:
        print('too big, guess lower')
        continue
    elif x == y:
        print('BINGO!, the number is {}'.format(x))
        break