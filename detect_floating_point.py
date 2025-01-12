# You are given a string N.
# Your task is to verify that N is a floating point number.

import re

def is_valid_float(s):
    
    pattern = r'^[+-]?(\d+\.\d+|\.\d+)$'
    return bool(re.match(pattern, s))
T = int(input())
for i in range(T):
    s = input().strip()
    try:
        if is_valid_float(s):
            float(s)  
            print(True)
        else:
            print(False)
    except ValueError:
        print(False)