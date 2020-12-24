week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
weekend = ['Sat', 'Sun']
week.extend(weekend)
for i,j in enumerate(week):
    print(i+1, j)