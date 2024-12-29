# You are given a string S.
# Your task is to find the indices of the start and end of string k in S

strr=input()
substr=input()

len_main=len(strr)
len_sub=len(substr)
isfound=False
for i in range(0,len_main):
    sub_string=strr[i:i+len_sub]
    if sub_string==substr:
        print(f"({i}, {i+len_sub-1})")
        isfound=True
if isfound==False:
 print("(-1, -1)")