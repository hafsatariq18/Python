# You are given a string S.
# Your task is to print all possible permutations of size k of the string 
# in lexicographic sorted order.

from itertools import permutations

S, k = input().split()
S = sorted(S.upper())
k = int(k)

for i in permutations(S,k):
  print("".join(i))