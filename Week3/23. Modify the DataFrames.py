import pandas as pd

list = [('Mayue', 3000), ('Lilin', 4500), ('Wuyun', 8000)]
aDF = pd.DataFrame(list, columns=['name','pay'])
aDF['tax'] = [0.05,0.05,0.1]
aDF.loc[5] = {'name': 'Liuxi', 'pay': 5000, 'tax': 0.05}
aDF['tax'] = 0.03
aDF.loc[5] = ['Liuxi', 9800, 0.05]
# = aDF.loc[: ['Liuxi', 9800, 0.05]]
aDF.iloc[:,[0,2,1]] # to change the order of columns
# = reindex()
print(aDF)