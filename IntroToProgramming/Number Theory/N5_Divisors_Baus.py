"""
Created on Wed Mar 27 12:06:05 2019

@author: bdbaus
"""

def divisors(n):
    divList = []
    for x in range(1,n//2+1):
        if n % x == 0 and n != x:
            divList.append(x)
    
    #continue
    
    return divList

print(divisors(100))


