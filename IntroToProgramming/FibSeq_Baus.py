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
        return fiblst
        print("All terms: ",fiblst)
        print("Last 10 terms: ",fiblst[-10:])

    
"""
#UNCOMMENT TO PROVIDE TEST LISTS 
  
Fib(0,1,0)
Fib(0,1,1)
Fib(0,1,2)
Fib(4,5,20)
"""

def cat(n,r):    
    sequence = Fib(0,1,10)
    #this is a list of the first 10 terms to prove catalin's identity
    term1=(sequence[n]**2)-(sequence[n-r]*sequence[n+r])
    term2=((-1)**(n-r))*(sequence[r]**2)
    print(term1,"=",term2)

#***N MUST BE GREATER THAN R*************
#PROOF OF CATALAN'S IDENTITY, works with all numbers that satisfy condition
    
cat(6,4)