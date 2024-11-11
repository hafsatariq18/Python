# List Palindrome Check

list1=[1,2,3,2,1]
list2=list1.copy()
list2.reverse()
if list1 == list2:
  print("The list is palindrome")
else:
  print("The list is not palindrome")

  

# String Palindrome_check

X = input()

output = ""
for i in X:
  output += i
output = X[::-1]
if output == X:
  print ("Palindrome")
else:
  print ("Not Palindrome")