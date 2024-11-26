# You are given a space separated list of nine integers. 
# Your task is to convert this list into a 3 X 3 NumPy array.

import numpy

arr = list(map(int, input().split()))
new_arr = numpy.array(arr)

new_arr.shape = (3, 3)
print(new_arr)