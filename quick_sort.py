# Algorithms - JeffE
# implemented by Joohoon Kim
import numpy as np
import random as rnd

#Inputs
A = rnd.sample(range(1,100),10)

def SWAP(Arr, a, b):
    temp = Arr[a]
    Arr[a] = Arr[b]
    Arr[b] = temp
    return Arr

def QUICKSORT(Arr):
    n = len(Arr)
    if(n > 1):
        p = (n-1)/2                         #pivot element
        r = PARTITION(Arr, p)
        QUICKSORT(Arr[0:r])
        QUICKSORT(Arr[r+1:n])
    return Arr

def PARTITION(Arr, p):
    n = len(Arr)
    SWAP(Arr,p,n-1)
    l = -1                              # num of items < pivot
    for i in range(0,n-1):
        if Arr[i] < Arr[n-1]:
            l = l+1
            SWAP(Arr,l,i)
    SWAP(Arr,n-1,l+1)
    return l+1

if __name__ == "__main__":
    print(A)
    A = QUICKSORT(A)
    print(A)
