# You are given the coefficients of a polynomial P.
# Your task is to find the value of P at point x.


import numpy

coefficients = list(map(float, input().split( )))
X = float(input())

value = numpy.polyval(coefficients, X)
print(value)
