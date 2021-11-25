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

def QUICKSORT(Arr,l,h):
    if(l < h):
        r = PARTITION(Arr, l, h)
        QUICKSORT(Arr,l,r-1)
        QUICKSORT(Arr,r+1,h)
    return Arr

def PARTITION(Arr,l,h):
    idx = l
    p = Arr[l]
    while l < h:
        while l < len(Arr) and Arr[l] <= p:
            l += 1

        while Arr[h] > p:
            h -= 1
            
        if l < h:
            SWAP(Arr,l,h)

    SWAP(Arr,idx,h)
    return h

if __name__ == "__main__":
    print(A)
    A = QUICKSORT(A,0,len(A)-1)
    print(A)
