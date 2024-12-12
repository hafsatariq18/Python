# You are given three integers: a, b, and m. Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).


a = int(input())
b = int(input())
m = int(input())

power = pow(a, b)
result = pow(a, b, m)

print(power)
print(result)