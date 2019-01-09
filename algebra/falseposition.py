""" a program to implement false position method for finding root """
# Dhruv Suthar [ github/dhrvsthr ]
# Website: dhrvsthr.ml
# Python 3.7.2

# Function 'f(x)' returns the functional value at 'x'
# Function 'opp(a,b)' returns Boolean value based on sign of 'a' and 'b' checking if opposite or not
# Function 'flps(fn,lf,rg)' returns the midpoint after assert areopp() and further computing midpoint

import math
def f(x):
    return x**3 - (5*x) -6

def opp(a,b):
    return a*b<0

def falsepos(fn,lf,rg):
    assert opp(fn(lf),fn(rg))
    for i in range(7):
        md = ((lf*fn(rg))-(rg*fn(lf)))/(fn(rg)-fn(lf))
        if(opp(fn(lf),fn(md))):
            rg=md
        else:
            lf=md
        print("x",i+1," f(x) = ",f(md),"[",lf,rg,"]","[",f(lf),f(rg),"]")
    return md

x = flps(f,2,3)
print(x)
