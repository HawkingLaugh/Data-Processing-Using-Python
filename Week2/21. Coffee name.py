def cleanList(list):
    editList = []
    for item in list:
        for name in item:
            """ 
            str.isalpha() check the str is alphabet or not, if str(name) is not alphabet, 
            replace them into blank. the result have to apply back into item itself
            """
            if name.isalpha() != True:
                item = item.replace(name, '')
        editList.append(item)
    return editList

originList = ['32Latte', '_Americano30', '/34Cappuccion', 'Mocha35']
cleanedList = cleanList(originList)
for i,j in enumerate(cleanedList):
    print(i+1,j)
# ==
for k,l in zip(range(1, len(cleanedList) + 1), cleanedList):
    print(k,l)