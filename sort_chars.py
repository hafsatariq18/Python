# You are given a string S.
# S contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

S = str(input())
S2 = sorted(list(S))
for i in S2:
  if i.isalpha() and i.islower():
   print(i, end = '')
for i in S2:
  if i.isalpha() and i.isupper():
   print(i, end = '')

for i in S2:
  if i.isdigit():
    value = int(i)
    if value %2!=0:
      print(i, end = '')
for i in S2:
  if i.isdigit():
    value = int(i)
    if value %2==0:
      print(i, end = '')