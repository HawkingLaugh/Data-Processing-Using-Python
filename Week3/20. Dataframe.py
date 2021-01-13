import pandas as pd
import numpy as np

data = {'name':['Amy', 'David', 'Lance'], 'pay':[4000,5000,6000]}
frame = pd.DataFrame(data)

d2 = np.array([('Amy', 4000), ('David', 5000), ('Lance', 6000)])
f2 = pd.DataFrame(d2, index = range(1,4), columns=['name', 'pay'])
print(frame[frame.pay >= 5000])
