import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6), dpi = 100)
plt.title('Plot Example')
plt.xlabel('X label')
plt.ylabel('Y label')
t = np.arange(0.,4.,0.1)

plt.plot(t,t,color='red', linestyle='-', linewidth=3,label='Line1')
plt.plot(t, t+2, color='green',linestyle='', marker='*', linewidth=3,label='Line2')
plt.plot(t, t**2, color='blue',linestyle='', marker='+', linewidth=3,label='Line3')
plt.legend(loc='upper left')
plt.show()