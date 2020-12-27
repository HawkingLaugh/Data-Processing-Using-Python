import operator

sStr = 'acdhdca'
if operator.eq(sStr, sStr.join(reversed(sStr)))==0:
    print('Yes')
else:
    print('no')