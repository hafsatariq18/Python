# There is an array of n integers. There are also 2 disjoint sets,A  and B, each 
# containing m integers. You like all the integers in set A and dislike all the 
# integers in set B. Your initial happiness is 0. For each i integer in the array, 
# if i belongs to A, you add 1 to your happiness. If i belongs to B, you add -1 to 
# your happiness. Otherwise, your happiness does not change. Output your final 
# happiness at the end

n, m = map(int, input().split( ))
array = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in array:
  if i in A:
    count += 1
  elif i in B:
    count -= 1
print(count)