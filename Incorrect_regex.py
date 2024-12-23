# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

import re
x = int(input())
case = (input() for i in range(x))

for pattern in case:
    try:
        re.compile(pattern)  
        print(True)
    except re.error:
        print(False)