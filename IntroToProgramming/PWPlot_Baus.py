"""
I.7

@author: bdbaus
"""

import matplotlib.pyplot as plt
import numpy as np

def func(x,N):
    def f(x):
        if(x < -2): 
            return -3*(x+2)**2+1
        elif -2 <= x < -1:
            return 1
        elif -1 <= x <= 1:
            return (x-1)**3+3
        elif 1 < x < 2:
            return np.sin(np.pi*x)+3
        elif x >= 2:
            return 3*(np.sqrt(x-2))+4
        return 0.0

    f2 = np.vectorize(f)
    
    x = np.linspace(0., 10., N)

    y = f2(x)

    plt.plot(x,y, '-')

    plt.xlim([-3,3])

    plt.show()
    
func(x,1000)