import numpy as np 
import matplotlib.pyplot as plt 
import math as m

v = 30
g= 9.8

theta = np.arange(m.pi/6, m.pi/3, m.pi/36)

t = np.linspace(0,5, num =100)

for i in theta:
    empty_array1 = []
    empty_array2 = []

    for j in t:

        x = ((v*j)*np.cos(i))
        y = ((v*j)*np.sin(i)) - ((0.5*g)*(j**2))



        empty_array1.append(x)
        empty_array2.append(y)
    p = [i for i, j in enumerate(empty_array2) if j < 0]                        
    for i in sorted(p, reverse = True):
        del empty_array1[i]
        del empty_array2[i]
    plt.plot(empty_array1, empty_array2)

plt.show()