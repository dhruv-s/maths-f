""" a program to implement false position method for finding root """
# Dhruv Suthar [ github/dhrvsthr ]
# Website: dhrvsthr.ml
# Python 3.7.2

import math
def f(x):
    return x**3 - (5*x) -6

def opp(a,b):
    return a*b<0

def falsepos(fn,lf,rg):
    assert opp(fn(lf),fn(rg))
    for i in range(7):
$ head falseposition.py 12
==> falseposition.py <==
import math
def f(x):
    return x**3 - (5*x) -6

def opp(a,b):
    return a*b<0

def falsepos(fn,lf,rg):
    assert opp(fn(lf),fn(rg))
    for i in range(7):
head: cannot open '12' for reading: No such file or directory
$ head -n 30 falseposition.py
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

x = falsepos(f,2,3)
print(x)
