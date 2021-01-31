import pandas as pd
# import Lagrange interpolation functions
from scipy.interpolate import lagrange

df = pd.read_excel("nan.xlsx")

#   name     A     B     C
# 0    a  56.0  87.0  90.0
# 1    b   NaN  89.0  78.0
# 2    c  67.0  66.0  75.0
# 3    d  97.0   NaN   NaN
# 4    e   NaN  92.0  74.0
# 5    f  82.0  75.0   NaN

for i in df.columns:
  for j in range(len(df)):
    # interpolate it if it is nan
    if (df[i].isnull())[j]:
      # Set the number of before and after to be 3, the default is 5
       k = 3
       # pick up the data
       y = df[i][list(range(j-k, j)) + list(range(j+1, j+1+k))]
       # remove the null value from the selected number 
       y = y[y.notnull()]
       df[i][j] = lagrange(y.index, list(y))(j)
print(df)

# the output is as below
# name        A    B    C
# 0 a 56.000000 87.0 90.0
# 1 b 53.333333 89.0 78.0
# 2 c 67.000000 66.0 75.0
# 3 d 97.000000 68.7 75.5
# 4 e 112.333333 92.0 74.0
# 5 f 82.000000 75.0 70.5