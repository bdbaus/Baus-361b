"""
Created on Tue Mar 19 20:46:23 2019

@author: bdbaus
"""

import numpy as np

#every odd composite number can be written as the sum of a prime and twice a square
# P = i + 2k^2


#modified prime checking function from previous assignment
def primecheck(n):
    if n >= 2:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    else:
        return False
  
##########################

num = 3 #This cannot be 2, it is 3 becuase that is the FIRST ODD PRIME

primeList=[2]#begins already containing the first prime (it will be used to loop through to find valid N values)

cond = True #only used to keep the loop going

while cond: #will continuously run
    if primecheck(num): #check if odd number is a prime, if it is, add to list. 
        primeList.append(num)
   
    else: #checking ODD COMPOSITES, if its not prime it will check if k is an integer, k = int(k), 
    # if it is an integer, it will check it again with all the subsequent primes.
    # when k is not an integer, it will print that value of k
        
        for prime in primeList: #checks for n value where 
            if  (np.sqrt((num-prime)/2))==int(np.sqrt((num-prime)/2)): 
                break
        
        else: #ONLY executed when k does not equal an integer 
            print(num)
            break
    
    num += 2 #THIS makes all numbers being checked that are NOt prime, be ODD

