# Read four numbers, a, b, c, and d, and print the result of a^b + c^d.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = pow(a, b) + pow(c, d)
print(result)