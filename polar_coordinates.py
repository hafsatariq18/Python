# Task
# You are given a complex z. Your task is to convert it to polar coordinates.

import cmath
x = complex(input())

r = abs(x)
print(r)

result = cmath.phase(complex(x))
print(result)