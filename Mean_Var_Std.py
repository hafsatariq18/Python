# You are given a 2-D array of size N X M.
# Your task is to find:

# The mean along axis 1
# The var along axis 0
# The std along axis None

import numpy

N,M = map(int, input().split( ))
array = numpy.array([list(map(int, input().split( ))) for i in range (N)])

mean = numpy.mean(array, axis = 1)
print(mean)

variance = numpy.var(array, axis = 0)
print(variance)

std_deviation = numpy.std(array)
if std_deviation == 0.0:
    print(0.0)  
else:
    print("{:.11f}".format(std_deviation))