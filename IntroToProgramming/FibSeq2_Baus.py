"""
I.6

@author: bdbaus
"""


def Fib(N,m):
    fiblst=[0,1]
    multlst=[]
    for i in range(2,N+1):
        fiblst.append(fiblst[i-1]+fiblst[i-2])
    #print(fiblst)
    
    
    for x in fiblst:
        if x % m == 0:
            multlst.append(x)
    #print("List of #'s divisible by m: ", multlst)
    print(len(multlst)," terms divisible by ",m)
    return multlst

Fib(10,2)
                
        