#https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

def arrays(arr):

    wills_array = numpy.array(arr, float)
    wills_array = wills_array[::-1]
    return wills_array
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)