# Your task is to print an array of size N X M with its main diagonal elements as 
# 1's and 0's everywhere else.

import numpy

numpy.set_printoptions(legacy="1.13")
N,M = map(int, input().split( ))
print(numpy.eye(N,M))