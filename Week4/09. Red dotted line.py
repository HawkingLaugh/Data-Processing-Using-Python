import numpy as np
import matplotlib.pyplot as plt
  
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.title('Red Dotted')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, y, 'r.')
plt.show()