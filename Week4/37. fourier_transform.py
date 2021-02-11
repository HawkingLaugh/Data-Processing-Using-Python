#%%
import scipy as sp
import matplotlib.pyplot as plt

listA = sp.ones(500)
listA[100:300] = -1
f = sp.fft(listA)
plt.plot(f)
# %%
