# You are given a 1-D array, A. Your task is to print the floor, ceil and  
# rint of all the elements of A.

import numpy
numpy.set_printoptions(legacy = "1.13")

A = numpy.array(list(map(float, input().split( ))))
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
