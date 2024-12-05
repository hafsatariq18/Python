# You are given a square matrix A with dimensions N X M. Your task is to find the 
# determinant. Note: Round the answer to 2 places after the decimal.


import numpy

N = int(input())
array = numpy.array([list(map(float, input().split( ))) for i in range (N)])
deteminant = numpy.linalg.det(array)

if deteminant == int(deteminant):
    print(float(deteminant))
else:
    print("{:.2f}".format(deteminant))