"""
Created on Mon Apr 15 12:03:25 2019

@author: bdbaus
"""
#MUST BE ENTERED IN REVERSE ORDER

p = [-5,4,0,3]
pointC = 2

#aka = x^3 + 4x -5

pLength = len(p)

def eVal(p,c):
    final=0
    for i in range(0,pLength-1):
        final+= p[i]*c**i
    return final
    
def derive(p):
    pPrime=[]
    for i,x in enumerate(p):
        q=i*x
        pPrime.append(q)
    return pPrime[1:]

def dif(p):
    return [c*(len(p)-i) for i, c in enumerate(p[:-1])]

#returns list containing elements of p' in reverse
    
    
def integral(p,a,b):
    p=p
    for i,p in enumerate(reversed(p)):
        return sum(p/(i+1))
    
    
pc=eVal(p,pointC)

p_prime=dif(p)

p_primec=eVal(p_prime,pointC)

print(p_prime)
#print(integral(p,0,1))
    
    
