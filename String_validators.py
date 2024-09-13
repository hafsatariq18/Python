# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Input Format

# # A single line containing a string S.

# # Constraints


# # Output Format

# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input()
x = []
for i in s:
  if i.isalnum():
      x.append(True) 
  else :
      x.append(False)
# print(x)


y = []
for i in s:
  if i.isalpha():
      y.append(True)
  else :
      y.append(False)
# print(y)

z = []
for i in s:
  if i.isdigit():
     z.append(True) 
  else:
    z.append(False)
# print(z)

w = []
for i in s:
  if i.islower():
     w.append(True) 
  else:
    w.append(False)
# print(w)

v = []
for i in s:
  if i.isupper():
     v.append(True) 
  else:
    v.append(False)
# print(v)


for item in [x, y, z, w, v]:
    print(True if True in item else False)