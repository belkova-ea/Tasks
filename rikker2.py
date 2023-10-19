import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import fsolve

a_array = [7.39]

for i in range(1, 510):
    a_array.append(a_array[i-1]+0.01)

y_max = []
y_mid = []
y_min = []
    
    
for i in range(len(a_array)):
    a = a_array[i]
    
    y_line = []
    for i in range(0, 51):
        y_line.append(math.log(a)*2)
    
    y = []
    
    for n in range(0, 51):
        y.append((n/10)*(1+a*math.exp(-n/10)))
        
    x = []
    for i in range(0, 51):
        x.append(i/10)
    
    
    intersections = []
    for i in range(len(x)):
        if y[i] == y_line[i]:
            intersections.append((x[i], y[i]))
        elif y[i] < y_line[i]:
            if i > 0 and y[i-1] > y_line[i-1]:
                # Использовать линейную интерполяцию для нахождения точки пересечения
                x_intersect = x[i-1] + (x[i] - x[i-1]) * (y_line[i] - y[i-1]) / (y[i] - y[i-1])
                intersections.append(x_intersect)
        elif y[i] > y_line[i]:
            if i > 0 and y[i-1] < y_line[i-1]:
                # Использовать линейную интерполяцию для нахождения точки пересечения
                x_intersect = x[i-1] + (x[i] - x[i-1]) * (y_line[i] - y[i-1]) / (y[i] - y[i-1])
                intersections.append(x_intersect)
                
    try:
       y_min.append(intersections[0])
    except:
        continue
    try:
       y_mid.append(intersections[1])
    except:
        continue
    try:
       y_max.append(intersections[2])
    except:
        continue

y_min = y_min[:-2]
a_array = a_array[:-2]
y_graph = []
for i in range(0, len(y_min)):
    y_graph.append(y_max[i]/y_min[i])
    print(a_array[i], y_min[i], y_mid[i], y_max[i])


plt.plot(a_array,y_graph)
plt.show()
