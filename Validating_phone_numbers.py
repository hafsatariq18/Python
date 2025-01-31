# # You are given some input, and you are required to check whether they are valid mobile numbers.
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.

import re
X = int(input())
numbers = [input()for i in range (X)]
pattern = r'^[987]\d{9}$'
for num in numbers:
    if re.fullmatch(pattern, num):
      print("YES")
    else:
      print("NO")