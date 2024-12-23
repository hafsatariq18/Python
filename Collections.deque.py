# Perform append, pop, popleft and appendleft methods on an empty deque d.

from collections import deque

N = int(input())
methods = (input().split( ) for i in range (N))
d = deque()
for method in methods:
    if method[0] == "append":
        d.append(int(method[1]))
    elif method[0] == "appendleft":
        d.appendleft(int(method[1]))
    elif method[0] == "pop":
        d.pop()
    elif method[0] == "popleft":
        d.popleft()
print(" ".join(map(str, d)))