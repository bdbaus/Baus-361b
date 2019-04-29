"""
Created on Mon Mar 25 12:10:16 2019

@author: bdbaus
"""

#ask for Zm
m=11

Flist = []

#a * b = 1

for z in range(1,m):
    for a in range(1,m):
        if (z*a)%m==1:
            Flist.append([z,a])
                
        #continue
          
print("The ",len(Flist)-1," multiplicative inverses in Z",m," (excluding the identity [1,1] are \n",Flist[1:])
            
            
# of the numbers between 1 and M, if the gcd between value and M is 1, then its an inverse, otherwise not?
# all values relatively prime to M, have inverses. 