# You are given two arrays: A and B.
# Your task is to compute their inner and outer product.

import numpy

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(numpy.inner(A, B)) 
print(numpy.outer(A, B))