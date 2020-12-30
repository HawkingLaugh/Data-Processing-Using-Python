If = [('AXP', 'American Express Company', '78.51'),('BA', 'The Boeing Company', '184.76'), ('CAT', 'Caterpillar Inc.', '96.39'), ('CSCO', 'CISCO Systems', '33.71'),('CVX', 'Chevron Corporation', '106.09')]
aDict = {}
for i in range(len(If)):
    name = If[i][0]
    value = If[i][2]
    aDict[name] = value
print(aDict)