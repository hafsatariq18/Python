# You are given two integer arrays of size N X M and M X P 
# (N & M are rows, and P is the column). Your task is to concatenate 
# the arrays along axis 0 .


import numpy

N, M, P = map(int, input().split()) 
array1 = [list(map(int, input().split())) for i in range(N)] 
array2 = [list(map(int, input().split())) for i in range(M)]


print (numpy.concatenate((array1, array2), axis = 0))