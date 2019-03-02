"""
Created on Mon Feb 25 12:22:25 2019

@author: bdbaus
"""
import numpy as np

def func1(N):

    f_n = lambda n: 2
    g_n = lambda n: n**2+3

    a_n = lambda n: (1+((f_n(n))/(g_n(n))))

    terms = []
    c=1

    for ii in range(1,N+1):
        c*=a_n(ii)
        terms.append(c)
    
    print("first 15:")
    for term in terms[:15]:
        print(term)
     
    print("Last 15:")
    for term in terms[-15:]:
        print(term)

func1(1000)

def func2(N):

    f_n = lambda n: 2
    g_n = lambda n: n+3

    a_n = lambda n: (1+((f_n(n))/(g_n(n))))

    terms = []
    c=1

    for ii in range(1,N+1):
        c*=a_n(ii)
        terms.append(c)
    
    print("first 15:")
    for term in terms[:15]:
        print(term)
     
    print("Last 15:")
    for term in terms[-15:]:
        print(term)

func2(1000)

def func3(N):
    b=.5
    
    a_n = lambda n: 1+(b**n)
    
    terms = []
    c=1

    for ii in range(1,N+1):
        c*=a_n(ii)
        terms.append(c)
    
    print("first 15:")
    for term in terms[:15]:
        print(term)
     
    print("Last 15:")
    for term in terms[-15:]:
        print(term)
    
func3(1000)

def func4(N):
    b=2
    
    a_n = lambda n: 1+(b**n)
    
    terms = []
    c=1

    for ii in range(1,N+1):
        c*=a_n(ii)
        terms.append(c)
    
    print("first 15:")
    for term in terms[:15]:
        print(term)
     
    print("Last 15:")
    for term in terms[-15:]:
        print(term)
    
func4(1000)

