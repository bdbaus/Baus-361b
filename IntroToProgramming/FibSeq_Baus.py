"""
Fibonacci Sequence

@author: bdbaus
"""

def Fib(F0, F1, N):
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
        fiblst=[F0,F1]
        for i in range(2,N+1):
            fiblst.append(fiblst[i-1]+fiblst[i-2])
        #print("All terms: ",fiblst)
        print("Last 10 terms: ",fiblst[-10:])
        return fiblst
        


def cat(n,r):    
    sequence = Fib(0,1,10)
    term1=(sequence[n]**2)-(sequence[n-r]*sequence[n+r])
    term2=((-1)**(n-r))*(sequence[r]**2)
    print(term1,"=",term2)

#***N MUST BE GREATER THAN R*************
#PROOF OF CATALAN'S IDENTITY, works with all numbers that satisfy condition
    
def cas(n):
    
    sequence = Fib(0,1,n)
    caslst=[]
    #this is a list of the last 10 terms to prove catalin's identity
    for i in range(n):
        item1=(sequence[i]**2-(sequence[i+1])*(sequence[i-1]))
        caslst.append(item1)
        #caslst.append(term1)
        #print(term1,"=",term2)
    print(caslst[-10:])
  
#Fib(0,1,10)
#cat(6,4)
cas(10)

#BOTH HOLD TRUE SO LONG AS THE FIRST TERMS ARE 0,1