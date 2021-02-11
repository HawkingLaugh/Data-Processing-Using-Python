#%%
from nltk.corpus import  gutenberg
from nltk.probability import *

allwords = gutenberg.words('shakespeare-hamlet.txt')
# A frequency distribution for the outcomes
''' sx = all characters in allwords, and store into a list with lower case 
[sx.lower() for sx in allwords if sx.isalpha()]'''
fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()])

# get all unique values
print(fd2.B())

# get all values
print(fd2.N())

# output the front 20 values as a form of table
fd2.tabulate(20)
fd2.plot(20)
# cumulative = add up
fd2.plot(20, cumulative=True)
# %%
