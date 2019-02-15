"""
I.7

@author: bdbaus
"""

import matplotlib.pyplot as plt
import numpy as np

def func(x,N):
    
    x = np.linspace(-3, 3, N)
    
    
    
    def f(x):
        if(x.any() < -2): 
            return -3*(x+2)**2+1
        elif -2 <= x.any() < -1:
            return 1
        elif -1 <= x.any() <= 1:
            return (x-1)**3+3
        elif 1 < x < 2:
            return np.sin(np.pi*x)+3
        elif x >= 2:
            return 3*(np.sqrt(x.any()-2))+4
        return 0.0

 
    y = f(x)

    plt.plot(x,y, 'g-',linewidth=2.0)

    plt.show()
    
func(1,100)