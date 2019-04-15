"""
Created on Mon Apr  8 12:06:47 2019

@author: bdbaus
"""

import numpy as np
import math as m

#N = 100

#Tol = .0001

guess = 10

f = lambda x: (1/100)*((x**4)+(np.exp(1)-2-np.sqrt(2))*(x**3)+(2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*(x**2)+(2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1))*x+(3*np.sqrt(2)*np.exp(1)))

ff = lambda x: (1/100)*((4*x**3)+(np.exp(1)-2-np.sqrt(2))*(3*x**2)+(2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*(2*x)+(2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1)))

g = lambda x: m.tan(x) - x - 2 

gg = lambda x: (1/m.cos(x)**2)-1

flag = True

#initial iterate
    
def newton(f,ff,guess,N=100,Tol=.0001):
    
    x0 = guess
    tempTol=2*Tol
    
    xlist=[]
    
    counter = 0
    
    while tempTol > Tol :

        x1=x0 - (f(x0)/ff(x0))
        xlist.append(x1)
        tempTol=abs(x0-x1)
        x0=x1
        
        counter+=1
    
   
       
        
    print(xlist,counter,"times")
    return x0

#newton(f,ff,guess)
roots=newton(f,ff,guess)

print("f(x)=0 when x = %0.4f +/- %0.4f" % (roots,.0001))

roots2=newton(g,gg,guess)
print("f(x)=0 when x = %0.4f +/- %0.4f" % (roots2,.0001))