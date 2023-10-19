import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import fsolve

a = 12.49

y_line = []
for i in range(5, 51):
    y_line.append(math.log(a)*2)

y = []

for n in range(5, 51):
    y.append((n/10)*(1+a*math.exp(-n/10)))
    
x = []
for i in range(5, 51):
    x.append(i/10)

plt.plot(x, y)
plt.plot(x, y_line)
plt.show()
