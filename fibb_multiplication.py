"""
Fibonacci Multiplication

Obtained from Algorithms by Jeff E.
Written by David Joohoon Kim
"""

import numpy as np
import random as rnd

#Inputs
n=2
m=3

hold = 0
X = rnd.sample(range(1,10),m)
Y = rnd.sample(range(1,10),n)
Z = [None] * (m+n)
i = 0
j = 0

for k in range(0,n+m):
    for i in range(0,m):
        for j in range(0,n):
            if(i+j is k):
                hold = hold + X[i]*Y[j]
    Z[k] = hold % 10
    hold = int(hold/10)

print("X=", X)
print("Y=", Y)
print("X*Y=",Z)
