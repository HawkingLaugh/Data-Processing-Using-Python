import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,300)
plt.axes([.1,.1,0.8,0.8])
plt.plot(x,np.sin(x), color='r')

plt.axes([.3,.15,0.4,0.3])
plt.plot(x,np.cos(x), color='g')

plt.show()