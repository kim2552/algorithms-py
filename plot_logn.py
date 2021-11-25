import matplotlib.pyplot as plt
import numpy as np

Arr = range(0,10000)
count = 0
N_POINTS = [None] * len(Arr)

def BINARY_SEARCH(Arr, lower_indx, upper_indx, num):
    global count
    global N_POINTS
    n = upper_indx - lower_indx
    N_POINTS[count] = n
    count+=1

    if (n > 0):
        middle = int(lower_indx + (n / 2))
        if(Arr[middle] < num):
            lower_indx = middle
        if(Arr[middle] > num):
            upper_indx = middle
        if(Arr[middle] == num):
            print("%s is at index %s"%(num, middle))
            return
        BINARY_SEARCH(Arr, lower_indx, upper_indx, num)
    else:
        print("could not find number")

if __name__ == "__main__":
    num_of_interest = 4312
    if (num_of_interest <= Arr[len(Arr)-1]):
        BINARY_SEARCH(Arr, 0, len(Arr), num_of_interest)
    newdata = np.squeeze(N_POINTS)
    plt.plot(newdata)
    plt.show()
