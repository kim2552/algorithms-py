"""
Merge Sort

Obtained from Algorithms by Jeff E.
Implemented by David Joohoon Kim
"""

import numpy as np
import random as rnd

#Inputs
A = rnd.sample(range(1,100),33)
m = 0

def MERGESORT(Arr):
    n = len(Arr)
    if(n > 1):
        m = int(n/2)
        Arr[0:m] = MERGESORT(Arr[0:m])
        Arr[m:n] = MERGESORT(Arr[m:n])
        Arr = MERGE(Arr, m)
    return Arr


def MERGE(Arr, m):
    i = 0
    j = m
    n = len(Arr)
    B = [None] * (n)
    for k in range(0, n):
        if j > n-1:                         #n-1 because array is exclusive
            B[k] = Arr[i]
            i = i+1
        elif i > m-1:
            B[k] = Arr[j]
            j = j+1
        elif Arr[i] < Arr[j]:
            B[k] = Arr[i]
            i = i+1
        else:
            B[k] = Arr[j]
            j = j+1
#    for k in range(0,n):                   #In the textbook this is included
#        Arr[k] = B[k]
    return B 

if __name__ == "__main__":
    print(A)
    A = MERGESORT(A)
    print(A)
