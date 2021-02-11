#%%
from nltk.corpus import inaugural
from nltk import ConditionalFreqDist
from nltk.probability import FreqDist

fd3 = FreqDist([s for s in inaugural.words()])
print(fd3.freq('freedom'))

# count frequency of words length in decending order
cfd = ConditionalFreqDist((fileid, len(w)) 
for fileid in inaugural.fileids() for w in inaugural.words(fileid) if fileid > '1980' and fileid < '2010')

print(cfd.items())
cfd.plot()
# %%
