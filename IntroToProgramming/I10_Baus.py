"""

@author: bdbaus
"""
import numpy as np


def triple(N):
    N2=N//2
    x=np.zeros([0,4])
    for a in range(1,N2):
        for b in range(a+1,N2):
            for c in range(b+1,N2):
                if (a*a+b*b==c*c and a+b+c==N):
                    x=np.vstack([x,np.array([a,b,c,a+b+c])])
                    #return a, b, c
    #print(np.matrix(x))
    print(x[np.where(x[:,3]==1026)])
#i, j, k = triple(1026)
#print(i,j,k,i+j+k)
triple(1026)