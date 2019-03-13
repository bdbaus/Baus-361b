"""
Created on Mon Mar 11 11:59:16 2019

@author: bdbaus
"""

def collatz(a0,N):
    
    Clist=[a0]   #list
    c=1         #counter
    
    while a0 > 1:
        c=c+1
        if a0 % 2 == 0: #even check
            a0=a0/2
            Clist.append(a0)
            
                
        else: #odd check
            a0=(a0*3)+1
            Clist.append(a0)   
            
    
    
   
    print(c, "terms to reach 1")
    
    
    
    print(Clist,c)
        
collatz(6,100)
        