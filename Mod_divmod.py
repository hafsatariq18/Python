# Read in two integers, a and b, and print three lines.
# The first line is the integer division a//b (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: a%b .
# The third line prints the divmod of a and b.


a = int(input())
b = int(input())
integer_division = a//b
modulo_operator = a % b
divsion = divmod(a, b)

print(integer_division)
print(modulo_operator)
print(divsion)
