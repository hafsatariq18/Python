# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N 
# but do not exist in both.

X = int(input())
m = set(map(int, input().split())) 
Y = int(input())
n = set(map(int, input().split()))

s = (m.difference(n))
s2 = (n.difference(m))
z = s.union(s2)
for i in sorted(z):
    print (i)