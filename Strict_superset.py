# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.

# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

A = set(map(int, input().split())) 
n = int(input())
is_strict_superset = True
for _ in range(n):
    B = set(map(int, input().split())) 
    if not (A > B):  
        is_strict_superset = False 
        break  
print(is_strict_superset) 