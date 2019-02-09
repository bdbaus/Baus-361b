"""
I.4

@author: bdbaus
"""

import numpy as np

########################
#EQUATION 1
#N is total number of terms in the partial sequence

def ProdCalcOne(N):
    prod1=1 #CANT USE 0 HERE!
    ResultArray = []
    for ii in range(2,N+1):
        formula=((ii**3)-1)/((ii**3)+1)
        ResultArray.append(formula)
    for x in ResultArray:
        prod1*=x
        #print("term",ii-1,": ",formula)
        
    print("\n The product for the first ",N," terms is ",prod1,"\n")
    print("\n The first 15 terms are ",*ResultArray[:16],sep="\n")
    #really would like this to print line by line for aesthetic purposes
    print("\n The last 15 terms are ",*ResultArray[-15:],sep="\n")
    #the arrays are providing e+XX at the end, not ideal

#########################
    
print('Here is the partial product for the first 15 terms of the "P_n" sequence:\n')      
ProdCalcOne(15)
 
#########################
    
def ProdCalcTwo(N):
    prod2=1
    ResultArray = []
    for ii in range(1,N+1):
        temp=(np.exp(ii/100))/(ii**10)
        ResultArray.append(temp)
    for x in ResultArray:
        prod2*=x
    print("\n The partial product for the first ",N," terms is ",prod2,"\n")
    print("\n The first 15 terms are ",*ResultArray[:16],sep="\n")
    print("\n The last 15 terms are ",*ResultArray[-15:],sep="\n")
    
#########################

print('Here is the partial product for the first 15 terms of the "T_n" sequence:\n')
ProdCalcTwo(15)

#########################


def ProdCalcThree(N):
    prod2=1
    ResultArray = []
    for ii in range(1,N+1):
        temp=(1+(1/(ii**2)))
        ResultArray.append(temp)
    for x in ResultArray:
        prod2*=x
    print("\n The partial product for the first ",N," terms is ",prod2,"\n")
    print("\n The first 15 terms are ",*ResultArray[:16],sep="\n")
    print("\n The last 15 terms are ",*ResultArray[-15:],sep="\n")
  
#########################
    
    
print('Here is the partial product for the first 15 terms of the "U_n" sequence:\n')
ProdCalcThree(15000)
    
    
    
    
    
    
    
    
    
    
    
    