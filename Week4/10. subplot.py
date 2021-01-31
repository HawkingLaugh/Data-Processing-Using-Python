import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,300)
# plt.figure(1)
plt.subplot(211)
plt.plot(x,np.sin(x), color='r')
plt.subplot(212)
plt.plot(x,np.cos(x), color='g')
plt.show()