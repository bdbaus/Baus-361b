"""
Created on Mon Apr  8 12:06:47 2019

@author: bdbaus
"""

import numpy as np
import math as m

#N = 100

#Tol = .0001

x0 = 10

f = lambda x: (1/100)*((x**4)+(np.exp(1)-2-np.sqrt(2))*(x**3)+(2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*(x**2)+(2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1))*x+(3*np.sqrt(2)*np.exp(1)))

ff = lambda x: (1/100)*((4*x**3)+(np.exp(1)-2-np.sqrt(2))*(3*x**2)+(2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*(2*x)+(2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1)))

g = lambda x: m.tan(x) - x - 2 

gg = lambda x: (1/m.cos(x)**2)-1

flag = True

#initial iterate
    
def newton(f,ff,x0,N=100,Tol=.0001):
    
    xlist=[]
    counter = 0
    
    for i in range(N):
        
        if ff(x0)==0:
            return x0
        
        x1=x0 - (f(x0)/ff(x0))
        xlist.append(x1)
        counter+=1
        
        p = abs(x1-x0)
        
        if p < Tol:
            break
        
        x0=x1
    
    return x0,xlist,counter

print(newton(f,ff,x0))
print(newton(g,gg,x0))