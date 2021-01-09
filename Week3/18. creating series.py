import pandas as pd
import numpy as np
aSer = pd.Series([1,2.0,'a'])

bSer = pd.Series(['apple', 'peach', 'lemon'],index = [1,2,3])

aSer = pd.Series([3,5,7], index = ['a','b','c'])
print(np.exp(aSer))