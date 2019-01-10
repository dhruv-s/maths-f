""" a program to implement false position method for finding root """
# Dhruv Suthar [ Github/dhrvsthr ]
# Website: dhrvsthr.ml
# Python 3.7.2

# importing 'math' module

import math

# Function 'f(x)' returns the functional value at 'x'
# Function 'areopp(a,b)' returns Boolean value based on sign of 'a' and 'b' checking if opposite or not
# Function 'flps(fn,lf,rg)' returns the midpoint after assert areopp() and further computing midpoint
# 'flps()' function uses False Position Method for Root Finding

## Function Definitions and IMmportant Variables

# [any valid integer for iterations]
nit = 10

def f(x):
    return x - math.cos(x)
    # [any equation in terms of 'x']

def areopp(a,b):
    return a*b<0

def flps(lf,rg):
    assert areopp(f(lf),f(rg))
    for i in range(nit):
        md = ((lf*f(rg))-(rg*f(lf)))/(f(rg)-f(lf))
        print(md)
        if(areopp(f(lf),f(md))):
            rg=md
        else:
            lf=md
        # add print statement for traversal of values
    return md

x = flps(0.5,1)
print(x)
