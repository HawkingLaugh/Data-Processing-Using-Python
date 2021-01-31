#%%
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1,10,50)


# for labeling bins

bins = np.linspace(data.min(), data.max(), num = 3, endpoint='True')
plt.hist(data, bins=bins, rwidth=0.95, edgecolor='k')
# %%