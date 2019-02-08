"""
@author: bdbaus
"""

import numpy as np

def SumCalcOne(N):
    for i in range(1,N):
        sum1=0
        temp=(np.log((i**4)+i+3))/((np.sqrt(i))+3)
        sum1+=temp
        print(sum1)
        