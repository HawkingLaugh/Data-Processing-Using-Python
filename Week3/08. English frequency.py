text = '''The Lord is my shepherd; I shall not want.
He maketh me to lie down in green pastures: he leadeth me beside the still waters.
He restoreth my soul: he leadeth me in the paths of righteousness for his name's sake.
Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; thy rod and thy staff they comfort me.
Thou preparest a table before me in the presence of mine enemies: thou anointest my head with oil; my cup runneth over.
Surely goodness and mercy shall follow me all the days of my life: and I will dwell in the house of the Lord for ever.'''

tList = text.split()
tDict = {}
for i in tList:
    if not i.isalpha():
        tList.remove(i)
    if i not in tDict:
        tDict[i] = 1
    else:
        tDict[i] += 1
    '''
    or
    .get() returns the value of the key
    = dict[item], however, dict[item] will gen out error if item not exist
    if i not exist, create item and assign 0 to it, if exist, get the value and + 1
    tDict[i] = tDict.get(i,0) + 1
    '''
print(tDict)