"""

@author: bdbaus
"""

def prime_check(n):
    if(n==0 or n==1):
        return False
    #added this, would not work for 2 otherwise
    elif(n==2):
        return True
    else:
        for ii in range(3,n):
            if(n%ii==0 or n%2 == 0):
                return False
        return True
    
    
def find_prime(m):

    primelist=[]
    firstp=2
    #will stop at the Mth number of the list
    while(len(primelist)<m):
        #will add primes to empty list until the Mth prime appears
        if(prime_check(firstp)==True):
            primelist.append(firstp)
        firstp+=1
    #ends when the list reaches M length
    #for prime in primelist:
    #    print(prime)
    print(m,"th prime number is ",primelist[-1])
    return(primelist[-1])
    
    
find_prime(10)