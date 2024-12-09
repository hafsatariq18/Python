# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    reverse = arr[::-1]
    numpy_array = numpy.array(reverse, float)
    return numpy_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)