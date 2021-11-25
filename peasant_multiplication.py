"""
Peasent Multiplication
(1) determine parity (even or odd)
(2) add
(3) duplation (double a number)
(4) mediation (halve the number, rounding down)

Obtained from Algorithms by Jeff E.
Written by David Joohoon Kim
"""

import numpy as np
import random as rnd

#Inputs
x_orig = rnd.randint(0,500)
y_orig = rnd.randint(0,500)
x = x_orig
y = y_orig

prod = 0
while x > 0:
    if(x%2 != 0):
        prod = prod + y
    x = int(x/2)
    y = y+y

print("x=",x_orig)
print("y=",y_orig)
print("x*y=",prod)
