"""
Created on Wed Mar 27 12:36:17 2019

@author: bdbaus
"""

def divisors(n):
    divList = []
    for x in range(1,n//2+1):
        if n % x == 0 and n != x:
            divList.append(x)
    
    
    #continue
    
    return divList


def check(N):
    results = []
    
    for i in range(1,N+1):
        a = sum(divisors(i))
        if sum(divisors(a)) == i:
            results.append([a,i])
                
    print(results)
    
check(284)