# You are given a 2-D array with dimensions N X M.
# Your task is to perform the sum tool over axis 0 and then find the  
# product of that result.

import numpy

N,M = map(int, input().split( ))
array = numpy.array([list(map(int, input().split( )))for i in range(M)])

sum = (numpy.sum(array, axis = 0))
# print(sum)

print(numpy.product(sum))
