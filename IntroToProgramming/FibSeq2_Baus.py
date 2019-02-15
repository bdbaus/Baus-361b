"""
I.6

@author: bdbaus
"""

def Fib(N):
    fiblst=[]
    if N==0:
        fiblst=[]
        print(fiblst)
        return fiblst
    elif N==1:
        fiblst=[0]
        print(fiblst)
        return fiblst
    elif N==2:
        fiblst=[0,1]
        print(fiblst)
        return fiblst
    else:
        fiblst=[0,1]
        for i in range(2,N+1):
            fiblst.append(fiblst[i-1]+fiblst[i-2])
        print("All terms: ",fiblst)
        #print("Last 10 terms: ",fiblst[-10:])
        return fiblst

def Mult(N,m):
    fiblst=[0,1]
    multlst=[]
    for i in range(2,N+1):
        fiblst.append(fiblst[i-1]+fiblst[i-2])
    #print(fiblst)
    
    
    for x in fiblst:
        if x % m == 0:
            multlst.append(x)
    #print("List of #'s divisible by m: ", multlst)
    print((len(multlst)/N)*100,"% of the first ",N,"are divisible by ",m)
    return multlst

#Fib(16)
Mult(1000,10)
                
        