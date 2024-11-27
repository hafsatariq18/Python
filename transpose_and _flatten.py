# You are given a N X M integer array matrix with space separated elements 
# (N = rows and M = columns).
# Your task is to print the transpose and flatten results.


import numpy


N, M = map(int, input().split()) 
element = [list(map(int, input().split())) for i in range(N)] 

arr = numpy.array(element)

print(numpy.transpose(arr))
print(arr.flatten())

