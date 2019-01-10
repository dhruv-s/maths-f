""" a program to implement bisection method for finding root """
# Dhruv Suthar [ Github/dhrvsthr ]
# Website: dhrvsthr.ml
# Python 3.6.1

# importing 'math' module

import math

# Function 'f(x)' returns the functional value at 'x'
# Function 'areopp(a,b)' returns Boolean value based on sign of 'a' and 'b'
# Function 'bisect(fn,lf,rg)' returns the midpoint after assert areopp() and further computing midpoint
# 'bsct()' function uses Bisection Method for Root Finding

## Function Definitions and IMmportant Variables

# [any valid integer for iterations]
nit = 25

def f(x):
    return x - math.cos(x)
    # [any equation in terms of 'x']

def areopp(a,b):
    return a*b<0

def bsct(lf,rg):
    assert areopp(f(lf),f(rg))
    for i in range(nit):
        md = (lf+rg)/2.0
        print(md)
        if(areopp(f(lf),f(md))):
            rg=md
        else:
            lf=md
        # add print statement for traversal of values
    return md

## Main Program Run

x = bsct(0.5,1)
print(x)
