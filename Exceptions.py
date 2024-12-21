# You are given two values  a and b.
# Perform integer division and print a/b.

T = int(input())
for i in range(T):
  try:
    a, b = map(int, input().split())
    Division = a//b
    print(Division)
  except ZeroDivisionError as e:
    print ("Error Code:",e)
  except ValueError as e: 
    print("Error Code:",e)