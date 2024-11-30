# You are given two integer arrays, A and B of dimensions N X M.
# Your task is to perform the following operations:

# Add (A + B)
# Subtract (A - B)
# Multiply (A * B)
# Integer Division (A / B)
# Mod (A % B)
# Power (A ** B)


import numpy

N,M = (map(int, input().split( )))
a = numpy.array([list(map(int,input().split()))for i in range(N)])
b = numpy.array([list(map(int,input().split()))for i in range(N)])

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)