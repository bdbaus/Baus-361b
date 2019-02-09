"""
@author: bdbaus
"""

import numpy as np

########################
#EQUATION 1
#N is total number of terms in the partial sum sequence

def SumCalcOne(N):
    sum1=0
    ResultArray = np.empty([N+1])
    for ii in range(1,N+1):
        temp=(np.log((ii**4)+ii+3))/((np.sqrt(ii))+3)
        #not using this method print("term",ii,": ",temp)
        ResultArray[ii] = temp
        sum1+=temp
    print("The sum for the first ",N," terms is ",sum1,"\n")
    print("The first 15 terms are ",*ResultArray[:15],sep="\n")
    print("The last 15 terms are ",*ResultArray[-15:],sep="\n")

#########################
    
print('Here is the partial summation for the first 15 terms of the "S_n" sequence:\n')      
SumCalcOne(15)
 
#########################
       
def SumCalcTwo(N):
    sum1=0
    ResultArray = np.empty([N+1])
    for ii in range(1,N+1):
        temp=(np.exp(ii/100)/(ii**10))
        #print("term",ii,": ",temp)
        sum1+=temp
    print("The sum for the first ",N," terms is ",sum1,"\n")
    print("The first 15 terms are ",*ResultArray[:15],sep="\n")
    print("The last 15 terms are ",*ResultArray[-15:],sep="\n")
    
#########################

print('Here is the partial summation for the first 15 terms of the "T_n" sequence:\n')
SumCalcTwo(15)

#########################

def SumCalcThree(N):
    sum1=0
    ResultArray = np.empty([N+1])
    for ii in range(1,N+1):
        temp=(ii**2)*(np.pi/6)
        print("term",ii,": ",temp)
        ResultArray[ii]=temp
        sum1+=temp
    print("The sum for the first ",N," terms is ",sum1,"\n")
    print("\n The first 15 terms are ",*ResultArray[:15],sep="\n")
    print("\n The last 15 terms are ",*ResultArray[-15:],sep="\n")
    
#########################

print('Here is the partial summation for the first 15 terms of a sequence of my own creation:\n')
SumCalcThree(15)
