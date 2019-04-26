"""
Created on Wed Apr 17 12:31:48 2019

@author: bdbaus

*********************README******************************

This program conducts polynomial division to find the 
quotient "q" and remainder "r" for two polynimals.

These polynomails should be defined in a list such that
the first value is the constant, the second value has degree 1, 
the second value has degree 2, etc. For example:
    
f(x)= 2x^3 + x^2 + 5x + 3
f(x)= 3 + 5x + x^2 + 2x^3

f = [3,5,1,2]

Polynomails such as f(x) = 7x^2 + 3 are to be written with a 0 
in place of the missing x value as so:
    
    f = [3,0,7]
    
The two lists do not need to be of equal lengths, but it must be
true that len(f)>=len(g)
"""


####################################################################

f = [3,2,6]
# = 3+2x+6x^2

g=[1,3]
# = 1+3x


flength=len(f) #3
glength=len(g) #2

####################################################################
#ADDS 0s if not long enough

def pad(polylist,target_length):
    n=target_length-len(polylist)
    return polylist[:target_length]+[0]*n


####################################################################
    
def resizer(f,g):
    flength=len(f) #3
    glength=len(g) #2
    
    if flength < glength:
        f=pad(f,glength)
    elif glength < flength:
        g=pad(g,flength)
        
    print("f fixed up = ",f)
    print("g fixed up = ",g)
    return f,g

####################################################################

def degree(f):
    flen=len(f)
    degreeList=[]
    for i in range(flen):
        degreeList.append(i)
        
    return degreeList[len(degreeList)-1]

####################################################################

def LT(f):
    fLength=len(f) #3
    
    coeff=f[fLength-1] # f[3-1]=f[2]=6
    
    return coeff,fLength-1 #6

####################################################################

def divide(LTf,LTg,degf,degg):
    
    if len(g)>len(f):
        print("ERROR: denominator > numerator")
        
    else:
        degz=degf-degg
        
        z = LTf/LTg
        
        divided=[0]*(degz+1)     
        
        divided[degz]=z
        
    return divided

####################################################################

def ADD(f,g):
    combolist=[f,g]
    return[sum(i) for i in zip(*combolist)]
    #add corresponding list elements

####################################################################
    
def SUB(f,g):
    return[a-b for a,b in zip(f,g)]    

####################################################################

def mult(f,g):
    multiplied=[0]*(len(f)+len(g)-1)
    
    for i in range(len(f)):
        for j in range(len(g)):
            multiplied[i+j] += g[j]*f[i]
    
    newmult=pad(multiplied,(len(f)-1+len(g)-1))
    return newmult

####################################################################

    #([1,3,0],[3,2,6])
def deflator(f,g):
    
    print("f =",f)
    print("g =",g)
    
    q=[0]*len(f) #=[0,0,0]
    r=f #=[3,2,6]
    
    qfinal=[]
    
    count=0
    
    #degree(r)=2,degree(g)=1,
    while r != 0 and degree(g)<=degree(r):
        
        
        LTr,degr=LT(r) #=[6,2]
        LTg,degg=LT(g) #=[3,1]
        
        LTrDLTg=divide(LTr,LTg,degr,degg)
        
        q = ADD(q,LTrDLTg)
        val=q[len(q)-1]
        qfinal.append(val)
        
        gLTz=mult(LTrDLTg,g)
        
        r = SUB(r,gLTz)
        
        count+=1
        
    qfinal=qfinal[::-1]
    print("Quotient q =",qfinal)
    
    print("Remainder r =",r)
    
    return f,g,qfinal,r
    
deflator(f,g)
    
    
   


    