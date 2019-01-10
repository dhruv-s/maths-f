""" a program to implement false position method for finding root """
# Dhruv Suthar [ Github/dhrvsthr ]
# Website: dhrvsthr.ml
# Python 3.7.2

# importing 'math' module [basic library module]
# importing 'sympy' module as 's' [install using 'pip install sympy']

import math
import sympy as s

# Function 'f(fn)' returns the functional of 'fn' value at 'x'
# Function 'd(fn)' returns the derivative value of 'fn' at 'x'
# Function 'nwrp(lf,rg)' returns the midpoint does further computing midpoint
# 'nwrp()' function uses Newton Raphson Method for Root Finding

## Function Definitions and IMmportant Variables

# [any valid integer for iterations]
nit = 7

# declaring 'x' as symbol for 'sympy'
x = s.symbols('x')

def f(fn):
    fx = s.sympify(fn)
    return fx

def d(fn):
    dx = s.diff(f(fn))
    return dx

def nwrp(lf,rg):
    h1 = s.sympify(float(rg))
    # [any equation in terms of 'x']
    fn = "x - cos(x)"
    st = f(fn)/d(fn)
    for i in range(nit):
        h2 = h1 - st.subs(x,h1)
        h1 = h2
        print(h1.evalf())
    return h1

x2 = nwrp(0.5,1)
print(x2)
