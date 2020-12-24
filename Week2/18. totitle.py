aStr = 'What do you think of this saying "No pain, No gain"?'
# get the index of first "
# str.index('target', start, end)
lindex = aStr.index('\"', 0, len(aStr))
# get the index of second "
rindex = aStr.rindex('\"', 0, len(aStr))
tempStr = aStr[lindex+1:rindex]
# split by " and get the one with index[1]
tempStr2 = aStr.split("\"")[1]
print(tempStr2)
if tempStr.istitle():
    print('{} is title format'.format(tempStr))
else:
    print('{} is not title format'.format(tempStr))