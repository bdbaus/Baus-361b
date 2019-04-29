"""
Created on Mon Apr  8 12:40:43 2019

@author: bdbaus
"""

#number of possible tiles


n=5
r=2
b=3
g=4
 
def possible(r, n): #r is length of tile (2,3,4) and n is N slots
    
    possible = [1] + [0]*(n)
    #begins list with [1,...,0]
    print("POssible ways ",possible)
    #length = n+1
    print("length of possible is ",len(possible))
    
    for x in range(1, len(possible)): #1,n+1
        possible[x] += possible[x-1] #adds the first term to the second slot
        
        print("Possible[]",x,"is",possible)
        print("then")
        
        if x >= r: #when x reaches the length it makes the x index = possible[x-r]
            possible[x] += possible[x-r]
            print(possible)
            print("possible[]",x,"is",possible[x])
    return possible[x] - 1
    
    
print("Possiblities for red length 2 is ",possible(b,n))


#def e117(length):
#    
#    n=length
#    
#    possible = [1] + [0]*n
#    
#    for x in range(1,len(possible)):
#        possible[x] += sum(possible[max(n - 4,0) : x])
#    return str(possible[-1])
#
#print(e117(50))