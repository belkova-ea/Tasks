import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import integrate


def lambd(t):
    top = math.exp(1)**(- (t - b)**2 / 2*c)
    bottom = math.sqrt(2*math.pi*c)

    return top/bottom

Tb = 10
b = 5
c = 1
l = []
z = 7
integ = []
a = [0.1, 0.3, 0.5, 0.7, 1, 1.0455, 2, 3]

count = 0
t = 0
while (t <= Tb - a[z]):
    l.append(lambd(t))
    intg, err = integrate.quad(lambd, max(0, t - a[z]), t)
    integ.append(intg)
    t += 0.1
    count += 1

x = np.linspace (0, Tb - a[z], count)


print(l)


plt.plot(x, l)
plt.plot(x, integ)
plt.grid()
plt.show()
