#%%
import numpy as np
import matplotlib.pyplot as plt

# np.linspace(start, stop, num) to generate out a set of data
x = np.linspace(-np.pi,np.pi,256)
s = np.sin(x)
c = np.cos(x)

plt.title('Trigonometric Function')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,s)
plt.plot(x,c)
# %%
