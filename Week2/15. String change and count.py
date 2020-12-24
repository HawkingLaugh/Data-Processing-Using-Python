aStr = "Hello,World!"
bstr = aStr[:6] + 'Python!'
count = 0
for i in bstr:
    if i in ',.?!':
        count +=1
print('There are {} punctuation marks in bStr'.format(count))
print('There are {0:>5d} punctuation marks in bStr'.format(count))