"""
@author: bdbaus
"""

def calculator(x,y,z):
    ListOf=[]
    ListOf.append(x+y)
    ListOf.append((y*z)+(3*x))
    ListOf.append((ListOf[0])**2)
    ListOf.append((2*ListOf[1]-(x/2))/ListOf[0])
    ListOf.append(7%3)
    ListOf[2]=ListOf[2]+3
    ListOf[4]=ListOf[4]*(3/4)
    print("The sum of the elements of the list is ")
    print(round(sum(ListOf),2))
    
calculator(1,2,3)

