"""
Created on Mon Apr 15 12:03:25 2019

@author: bdbaus
"""
#MUST BE ENTERED IN REVERSE ORDER

p = [-1,2,-6,2]
pointC = 4
a=0
b=1

#[-5,4,0,1]
# = x^3 + 4x -5

pLength = len(p)


def eval2(p,pointC):
    return sum(pointC ** ((pLength)-i-1) * val for i, val in enumerate(p))


def derive(p):
    return [p[i] * i for i in range(1,pLength)]

#returns list containing elements of p' in reverse
    
    
def integral(p,a,b):
    final=0
    denom=float(pLength)
    for i in p:
        final += i/denom
        denom -= 1
    return final

def integral2(p,a,b):
    return sum(pVal / (i+1) for i, pVal in enumerate(reversed(p)))
    
    
pc=eval2(p,pointC)

p_prime=derive(p)

p_primec=eval2(p_prime,pointC)

p_integrated=integral2(p,a,b)

print(pc,"is the function evaluated at ",pointC)
print(p_prime,"is the coefficients of the derivative (such that the last element has the highest exponent)")
print(p_primec,"is the derivative evaluated at",pointC)
print(p_integrated,"is the definite integral of",p,"from",a,"to",b)
    
    
