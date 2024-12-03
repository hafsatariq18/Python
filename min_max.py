# You are given a 2-D array with dimensions N X M.
# Your task is to perform the min function over axis 1 and then find the max of that.

import numpy

N,M = map(int, input().split( ))
array = numpy.array([list(map(int, input().split( )))for i in range(N)])

min = (numpy.min(array, axis = 1))
# print(min)

print(numpy.max(min))