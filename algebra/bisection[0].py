""" a program to implement bisection method for finding root """
# Dhruv Suthar [ github/dhruv-s ]
# Python 3.6.1

import math

# Function 'f(x)' returns the functional value at 'x'
# Function 'areopp(a,b)' returns Boolean value based on sign of 'a' and 'b'
# Function 'bisect(fn,lf,rg)' returns the midpoint after assert areopp() and further computing midpoint

## Function Definitions

def f(x):   
    return (x**3)-(3*x)-5
    # [any equation in terms of 'x'] 

def areopp(a,b):
    return a*b<0

def bisect(fn,lf,rg):
    assert areopp(fn(lf),fn(rg))
    for i in range(256):
        md = (lf+rg)/2.000
        if(areopp(fn(lf),fn(rg))):
            rg=md
        else:
            lf=md
    return md

## Main Program Run

x = bisect(f,2,3)
print(x)
