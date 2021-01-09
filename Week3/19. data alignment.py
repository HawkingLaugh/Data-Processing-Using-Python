import pandas as pd

data = {'AXP':86.40, 'CSCO':122.64, 'BA':99.44}
sindex = ['AXP', 'CSCO', 'BA', 'AAPL']
aSer = pd.Series(data,index=sindex)

bSer = {'AXP':86.40, 'CSCO':122.64, 'CVX':23.78}
cSer = pd.Series(bSer)
print(aSer + cSer)