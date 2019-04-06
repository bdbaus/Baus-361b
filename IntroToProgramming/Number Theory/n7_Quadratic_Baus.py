"""
Created on Mon Apr  1 12:20:49 2019

@author: bdbaus
"""
import numpy as np

def prime(n):
    if n >= 2:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    else:
        return False

##############################
#ENTER TEST VALUE HERE
PP = 11
#############################


def qr(p):
    
    zList=[]
    
    for i in range(0,p):
        zList.append(i)   
            #print(zList)
            #[01234...p-1]
    
    rList=[]
        
    for k in range(0,(p+1)//2):
        n=((k**2) % p)
        
        #print(n,"is a quad res mod ",p)
            
        rList.append(n)
            
    #print(rList,"is the list of them for ",n)
    return p,len(rList)
        #print(counter,"QR for ",p)
        #print(count)
 
#qr()
        
#
if PP == 0:
    print([0,1])
elif PP == 1:
    print([1,1])
else:
    print("The left column contains the prime in Z",PP," and the right column contains how many quadratic residues for that prime")
    for p in range(PP+1):
        
        count = np.zeros([0,2])
        
        if prime(p):
            newrow = [qr(p)]
            
            count = np.vstack([count,newrow])
            
            print(count)
 
    
neg_one = np.zeros([0,2])  
    
for p in range(PP+1):
    if prime(p):
        for k in range(0,(PP+1)//2):
            if ((k**2)%PP) == (p-1):
                newrow2=(p,True)
                neg_one = np.vstack([neg_one,newrow2])
            
            else:
                newrow2=(p,False)
                neg_one = np.vstack([neg_one,newrow2])
                
#NEED TO FIX REPEATS CANT FIGURE HOW TO CHECK FOR REPEATED ELEMENTS
        
        
print("\n -1 in Z (mod",PP,")")
print("If a 1 appears once in the right column, the corresponding number to the left will have -1 as a quadratic residue.")
print(neg_one) 
        
        
        