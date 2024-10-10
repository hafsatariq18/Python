# You are given a two lists A  and B. Your task is to compute their 
# cartesian product AXB.

from itertools import product
x = [int(i) for i in input().split(' ')]
y = [int(i) for i in input().split(' ')]

result = product(x, y)
for pair in result:
    print(pair, end=' ')