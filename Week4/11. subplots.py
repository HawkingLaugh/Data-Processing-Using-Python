import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,300)
fig,(ax0,ax1) = plt.subplots(2,1)
ax0.plot(x,np.sin(x), color='r')
ax0.set_title('subplot1')

plt.subplots_adjust(hspace=0.5)

ax1.plot(x,np.cos(x), color='g')
ax1.set_title('subplot2')
plt.show()