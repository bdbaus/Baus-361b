"""
Created on Mon Mar 25 18:53:45 2019

@author: bdbaus
"""


#ask for Zm
m=8

#make list of Zm unnecessary
Zlist=[]
Flist = []

#must start at 1 because 0,1 cant be divisors
#** did not figure a way to do this without 2 loops...
for z in range(1,m):
    for a in range(1,m):
        i = z*a
        if i % m == 0:
            Zlist.append(z)
            Zlist.append(a)

for num in Zlist:
    if num not in Flist:
        Flist.append(num)
        
print(Flist,"are the ",len(Flist),"zero divisors of ",m,)



            #primes dont have it
            #if composit it is multiples of primes that compose it
            