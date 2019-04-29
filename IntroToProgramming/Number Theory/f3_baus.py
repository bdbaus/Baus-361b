"""
Created on Mon Apr  8 12:42:18 2019

@author: bdbaus
"""

num = 4

r=2
g=3
b=4

#calculate how many possibilities per color rgb, and number of slots num

def Squares(j,num):
    
    combos = j * (num-j+1)
    
print(Squares(b,num))