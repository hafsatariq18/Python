# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string 
# in lexicographic sorted order.

from itertools import combinations

S,k = input().split()
S = sorted(S.upper())
k = int(k)
for size in range(1,k+1):
  for i in combinations(S,size):
    print("".join(i)) 