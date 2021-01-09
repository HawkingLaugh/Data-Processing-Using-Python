import time
import math
import numpy as np

x = np.arange(0,100000,0.01)
print(x)
t_m1 = time.process_time()

for i, t in enumerate(x):
    x[i] = math.pow((math.sin(t)), 2)
t_m2 = time.process_time()

y = np.arange(0,100000,0.01)
t_n1 = time.process_time()
y = np.power(np.sin(y), 2)
t_n2 = time.process_time()

print('Running time of math: ' ,t_m2 - t_m1)
print('Running time of numpy: ' ,t_n2 - t_n1)