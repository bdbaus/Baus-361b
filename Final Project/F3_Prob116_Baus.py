"""
Created on Mon Apr  8 12:40:43 2019

@author: bdbaus
"""

#number of possible tiles


n=50
red=2
green=3
blue=4
 
def possible(m, n): #r is length of tile (2,3,4) and n is N slots
    
    possible = [1] + [0]*(n)
    #creates list of n + 1 length [1,0,0,0,0...n]
    
    
    
    for x in range(1, len(possible)): #1,n+1
        
        possible[x] += possible[x-1] #adds the preceding term to the next slot
        
        
        if x >= m: 
            print("x is greater than m")
   #when x reaches the length it makes the x index = that value + value of index[x-r]
            possible[x] += possible[x-m]
            
#            print(possible)
#            print("possible[]",x,"is",possible[x])
            
    return possible[x] - 1
    
    
print("Possiblities for tile row of length",n,"is",possible(red,n)+possible(blue,n)+possible(green,n))

    

##(x-2),(x-3),(x-4)
#
#def e117(length):
#    
#    n=length
#    
#    possible = [1] + [0]*(n)
#    
#    for x in range(1,len(possible)):
#        possible[n] += possible[n-2]
#                    += possible[n-3]
#                    += possible[n-4]
#    return sum of possibilities
#
#print(e117(50))