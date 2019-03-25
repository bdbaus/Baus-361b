"""
Created on Mon Mar 25 12:10:16 2019

@author: bdbaus
"""

#ask for Zm
m=9

Flist = []

#a * b = 1

for z in range(1,m):
    for a in range(1,m):
        if (z*a)%m==1:
            Flist.append([z,a])
                
        #continue
          
print("The ",len(Flist)-1," multiplicative inverses in Z",m," (excluding the identity [1,1] are \n",Flist[1:])
            
            
            