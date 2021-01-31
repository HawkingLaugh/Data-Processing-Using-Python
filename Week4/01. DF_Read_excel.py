import pandas as pd

a = pd.read_excel(io='scoreDF.xlsx')
b = a['Python'] + a['Math']
a['sum'] = b

a.to_excel('students.xlsx')